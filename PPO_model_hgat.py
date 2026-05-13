import copyimport copy
import math
import torch
import torch.nnimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(selfimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.reimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminalsimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj =import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj =import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        selfimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gatherimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logproimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adjimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_subimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opesimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


classimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_parasimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["deviceimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = trainimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochsimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgatimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_parasimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            modelimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.criticimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_parasimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.himport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actorimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopyimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'paramsimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.bimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_trainimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opesimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.featimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batchimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batchimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes,import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_subimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb =import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shapeimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb =import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb],import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action =import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(actionimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memoriesimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logproimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.opeimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memoriesimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(stateimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.rawimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batchimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligibleimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligible)
                memories.nums_opes.append(nums_opes)
                memories.action_indexesimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligible)
                memories.nums_opes.append(nums_opes)
                memories.action_indexes.append(action)
        
        return action
    
    def evaluate(self, state, action, ope_import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligible)
                memories.nums_opes.append(nums_opes)
                memories.action_indexes.append(action)
        
        return action
    
    def evaluate(self, state, action, ope_ma_adj, ope_pre_adj, ope_sub_adj, jobs_gather,import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligible)
                memories.nums_opes.append(nums_opes)
                memories.action_indexes.append(action)
        
        return action
    
    def evaluate(self, state, action, ope_ma_adj, ope_pre_adj, ope_sub_adj, jobs_gather, eligible):
        feat_opes = state.feat_opes_batch
        feat_mas =import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligible)
                memories.nums_opes.append(nums_opes)
                memories.action_indexes.append(action)
        
        return action
    
    def evaluate(self, state, action, ope_ma_adj, ope_pre_adj, ope_sub_adj, jobs_gather, eligible):
        feat_opes = state.feat_opes_batch
        feat_mas = state.feat_mas_batch
        
        ope_emb, ma_emb = self.hgatimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligible)
                memories.nums_opes.append(nums_opes)
                memories.action_indexes.append(action)
        
        return action
    
    def evaluate(self, state, action, ope_ma_adj, ope_pre_adj, ope_sub_adj, jobs_gather, eligible):
        feat_opes = state.feat_opes_batch
        feat_mas = state.feat_mas_batch
        
        ope_emb, ma_emb = self.hgat(feat_opes, feat_mas, ope_ma_adj, ope_pre_import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligible)
                memories.nums_opes.append(nums_opes)
                memories.action_indexes.append(action)
        
        return action
    
    def evaluate(self, state, action, ope_ma_adj, ope_pre_adj, ope_sub_adj, jobs_gather, eligible):
        feat_opes = state.feat_opes_batch
        feat_mas = state.feat_mas_batch
        
        ope_emb, ma_emb = self.hgat(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
        
        ope_emb = ope_emb.viewimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligible)
                memories.nums_opes.append(nums_opes)
                memories.action_indexes.append(action)
        
        return action
    
    def evaluate(self, state, action, ope_ma_adj, ope_pre_adj, ope_sub_adj, jobs_gather, eligible):
        feat_opes = state.feat_opes_batch
        feat_mas = state.feat_mas_batch
        
        ope_emb, ma_emb = self.hgat(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
        
        ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligible)
                memories.nums_opes.append(nums_opes)
                memories.action_indexes.append(action)
        
        return action
    
    def evaluate(self, state, action, ope_ma_adj, ope_pre_adj, ope_sub_adj, jobs_gather, eligible):
        feat_opes = state.feat_opes_batch
        feat_mas = state.feat_mas_batch
        
        ope_emb, ma_emb = self.hgat(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
        
        ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
        ma_emb = ma_emb.view(feat_mas.shape[0], -1,import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligible)
                memories.nums_opes.append(nums_opes)
                memories.action_indexes.append(action)
        
        return action
    
    def evaluate(self, state, action, ope_ma_adj, ope_pre_adj, ope_sub_adj, jobs_gather, eligible):
        feat_opes = state.feat_opes_batch
        feat_mas = state.feat_mas_batch
        
        ope_emb, ma_emb = self.hgat(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
        
        ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
        ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
        
        job_ma_emb = torch.gather(maimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligible)
                memories.nums_opes.append(nums_opes)
                memories.action_indexes.append(action)
        
        return action
    
    def evaluate(self, state, action, ope_ma_adj, ope_pre_adj, ope_sub_adj, jobs_gather, eligible):
        feat_opes = state.feat_opes_batch
        feat_mas = state.feat_mas_batch
        
        ope_emb, ma_emb = self.hgat(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
        
        ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
        ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
        
        job_ma_emb = torch.gather(ma_emb, 1, jobs_gather.unsqueeze(-1).expand(-1, -import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligible)
                memories.nums_opes.append(nums_opes)
                memories.action_indexes.append(action)
        
        return action
    
    def evaluate(self, state, action, ope_ma_adj, ope_pre_adj, ope_sub_adj, jobs_gather, eligible):
        feat_opes = state.feat_opes_batch
        feat_mas = state.feat_mas_batch
        
        ope_emb, ma_emb = self.hgat(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
        
        ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
        ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
        
        job_ma_emb = torch.gather(ma_emb, 1, jobs_gather.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1]))
        
        actor_input = torch.cat([ope_embimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligible)
                memories.nums_opes.append(nums_opes)
                memories.action_indexes.append(action)
        
        return action
    
    def evaluate(self, state, action, ope_ma_adj, ope_pre_adj, ope_sub_adj, jobs_gather, eligible):
        feat_opes = state.feat_opes_batch
        feat_mas = state.feat_mas_batch
        
        ope_emb, ma_emb = self.hgat(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
        
        ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
        ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
        
        job_ma_emb = torch.gather(ma_emb, 1, jobs_gather.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1]))
        
        actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
        action_logits = self.actorimport copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligible)
                memories.nums_opes.append(nums_opes)
                memories.action_indexes.append(action)
        
        return action
    
    def evaluate(self, state, action, ope_ma_adj, ope_pre_adj, ope_sub_adj, jobs_gather, eligible):
        feat_opes = state.feat_opes_batch
        feat_mas = state.feat_mas_batch
        
        ope_emb, ma_emb = self.hgat(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
        
        ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
        ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
        
        job_ma_emb = torch.gather(ma_emb, 1, jobs_gather.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1]))
        
        actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
        action_logits = self.actor(actor_input)
        action_logits = action_logits.masked_fill(~eligible,import copy
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
from graph.hgat import HGAT
from mlp import MLPCritic, MLPActor

class Memory:
    def __init__(self):
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []
        self.action_indexes = []
        
        self.ope_ma_adj = []
        self.ope_pre_adj = []
        self.ope_sub_adj = []
        self.batch_idxes = []
        self.raw_opes = []
        self.raw_mas = []
        self.proc_time = []
        self.jobs_gather = []
        self.eligible = []
        self.nums_opes = []
        
        
    def clear_memory(self):
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]
        del self.action_indexes[:]
        
        del self.ope_ma_adj[:]
        del self.ope_pre_adj[:]
        del self.ope_sub_adj[:]
        del self.batch_idxes[:]
        del self.raw_opes[:]
        del self.raw_mas[:]
        del self.proc_time[:]
        del self.jobs_gather[:]
        del self.eligible[:]
        del self.nums_opes[:]


class PPO_HGAT(nn.Module):
    def __init__(self, model_paras, train_paras):
        super(PPO_HGAT, self).__init__()
        self.device = model_paras["device"]
        self.lr = train_paras["lr"]
        self.betas = train_paras["betas"]
        self.gamma = train_paras["gamma"]
        self.eps_clip = train_paras["eps_clip"]
        self.K_epochs = train_paras["K_epochs"]
        self.A_coeff = train_paras["A_coeff"]
        self.vf_coeff = train_paras["vf_coeff"]
        self.entropy_coeff = train_paras["entropy_coeff"]
        self.minibatch_size = train_paras["minibatch_size"]
        
        self.hgat = HGAT(
            in_feats_ope=model_paras["in_size_ope"],
            in_feats_ma=model_paras["in_size_ma"],
            out_feats=model_paras["out_size_ope"],
            num_heads=[2, 2],
            dropout=model_paras["dropout"]
        ).to(self.device)
        
        self.actor = MLPActor(
            model_paras["actor_in_dim"],
            model_paras["n_latent_actor"],
            model_paras["n_hidden_actor"],
            model_paras["action_dim"]
        ).to(self.device)
        
        self.critic = MLPCritic(
            model_paras["critic_in_dim"],
            model_paras["n_latent_critic"],
            model_paras["n_hidden_critic"]
        ).to(self.device)
        
        self.policy_old = copy.deepcopy(self.hgat)
        self.policy_old_actor = copy.deepcopy(self.actor)
        self.policy_old_critic = copy.deepcopy(self.critic)
        
        self.optimizer = torch.optim.Adam([
            {'params': self.hgat.parameters()},
            {'params': self.actor.parameters()},
            {'params': self.critic.parameters()}
        ], lr=self.lr, betas=self.betas)
        
    def act(self, state, memories, dones, flag_sample=False, flag_train=True):
        with torch.no_grad():
            feat_opes = state.feat_opes_batch
            feat_mas = state.feat_mas_batch
            ope_ma_adj = state.ope_ma_adj_batch
            ope_pre_adj = state.ope_pre_adj_batch
            ope_sub_adj = state.ope_sub_adj_batch
            
            ope_emb, ma_emb = self.policy_old(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
            
            ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
            ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
            
            eligible = state.eligible_batch
            nums_opes = state.nums_opes_batch
            
            jobs = state.opes_appertain_batch
            jobs_gather = jobs.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1])
            job_ma_emb = torch.gather(ma_emb, 1, jobs_gather)
            
            actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
            action_logits = self.policy_old_actor(actor_input)
            
            action_logits = action_logits.masked_fill(~eligible, float('-inf'))
            dist = Categorical(F.softmax(action_logits, dim=-1))
            
            if flag_sample:
                action = dist.sample()
            else:
                action = torch.argmax(action_logits, dim=-1)
            
            logprob = dist.log_prob(action)
            
            if flag_train:
                memories.states.append(state)
                memories.logprobs.append(logprob)
                memories.ope_ma_adj.append(ope_ma_adj)
                memories.ope_pre_adj.append(ope_pre_adj)
                memories.ope_sub_adj.append(ope_sub_adj)
                memories.batch_idxes.append(state.batch_idxes)
                memories.raw_opes.append(feat_opes)
                memories.raw_mas.append(feat_mas)
                memories.proc_time.append(state.proc_times_batch)
                memories.jobs_gather.append(jobs)
                memories.eligible.append(eligible)
                memories.nums_opes.append(nums_opes)
                memories.action_indexes.append(action)
        
        return action
    
    def evaluate(self, state, action, ope_ma_adj, ope_pre_adj, ope_sub_adj, jobs_gather, eligible):
        feat_opes = state.feat_opes_batch
        feat_mas = state.feat_mas_batch
        
        ope_emb, ma_emb = self.hgat(feat_opes, feat_mas, ope_ma_adj, ope_pre_adj, ope_sub_adj)
        
        ope_emb = ope_emb.view(feat_opes.shape[0], -1, ope_emb.shape[-1])
        ma_emb = ma_emb.view(feat_mas.shape[0], -1, ma_emb.shape[-1])
        
        job_ma_emb = torch.gather(ma_emb, 1, jobs_gather.unsqueeze(-1).expand(-1, -1, ma_emb.shape[-1]))
        
        actor_input = torch.cat([ope_emb, job_ma_emb], dim=-1)
        action_logits = self.actor(actor_input)
        action_logits = action_logits.masked_fill(~eligible, float('-inf'))
        
        dist = Categorical(F.softmax(action_logits, dim