import torch
from torch import nn
import torch.nn.functional as F

class HGATLayer(nn.Module):
    def __init__(self, in_feats, out_feats, num_heads, dropout=0.0, concat=True):
        super(HGATLayer, self).__init__()
        self.num_heads = num_heads
        self.out_feats = out_feats
        self.concat = concat
        
        self.fc = nn.Linear(in_feats, out_feats * num_heads, bias=False)
        self.attn_l = nn.Parameter(torch.FloatTensor(size=(1, num_heads, out_feats)))
        self.attn_r = nn.Parameter(torch.FloatTensor(size=(1, num_heads, out_feats)))
        
        self.dropout = nn.Dropout(dropout)
        self.leaky_relu = nn.LeakyReLU(0.2)
        
        self.reset_parameters()
    
    def reset_parameters(self):
        gain = nn.init.calculate_gain('relu')
        nn.init.xavier_normal_(self.fc.weight, gain=gain)
        nn.init.xavier_normal_(self.attn_l, gain=gain)
        nn.init.xavier_normal_(self.attn_r, gain=gain)
    
    def forward(self, x, adj):
        h = self.fc(x).view(-1, self.num_heads, self.out_feats)
        
        el = (h * self.attn_l).sum(dim=-1).unsqueeze(-1)
        er = (h * self.attn_r).sum(dim=-1).unsqueeze(-1)
        
        attention = self.leaky_relu(el + er.transpose(1, 2))
        attention = torch.where(adj > 0, attention, torch.full_like(attention, float('-inf')))
        attention = F.softmax(attention, dim=-1)
        attention = self.dropout(attention)
        
        output = torch.matmul(attention, h)
        
        if self.concat:
            return output.view(-1, self.num_heads * self.out_feats)
        else:
            return output.mean(dim=1)

class HGAT(nn.Module):
    def __init__(self, in_feats_ope, in_feats_ma, out_feats, num_heads=[2, 2], dropout=0.0):
        super(HGAT, self).__init__()
        
        self.layer_ope1 = HGATLayer(in_feats_ope, out_feats, num_heads[0], dropout)
        self.layer_ope2 = HGATLayer(out_feats * num_heads[0], out_feats, num_heads[1], dropout)
        
        self.layer_ma1 = HGATLayer(in_feats_ma, out_feats, num_heads[0], dropout)
        self.layer_ma2 = HGATLayer(out_feats * num_heads[0], out_feats, num_heads[1], dropout)
        
        self.ope_ma_attn = nn.Parameter(torch.FloatTensor(size=(1, out_feats * num_heads[1], out_feats * num_heads[1])))
        
    def forward(self, feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj):
        ope_adj = ope_pre_adj + ope_sub_adj
        
        ope_h1 = self.layer_ope1(feat_opes, ope_adj)
        ope_h2 = self.layer_ope2(F.relu(ope_h1), ope_adj)
        
        ma_h1 = self.layer_ma1(feat_mas, ope_ma_adj.transpose(1, 2))
        ma_h2 = self.layer_ma2(F.relu(ma_h1), ope_ma_adj.transpose(1, 2))
        
        cross_attn = F.softmax(torch.matmul(ope_h2.unsqueeze(1), self.ope_ma_attn).matmul(ma_h2.unsqueeze(-1)).squeeze(-1), dim=-1)
        ope_h2 = ope_h2 + torch.matmul(cross_attn, ma_h2)
        
        return ope_h2, ma_h2
