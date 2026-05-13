#!/usr/bin/env python
"""
简化的训练脚本 - 用于训练改进后的模型
"""
import sys
import os
import json
import random
import time
import copy
import numpy as np
import torch

sys.path.insert(0, '.')

import PPO_model
from env.case_generator import CaseGenerator
from env.fjsp_env import FJSPEnv


def setup_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True


def main():
    SEED = 42
    setup_seed(SEED)
    
    print("=" * 60)
    print("训练改进模型 (启发式特征增强)")
    print("=" * 60)
    
    # 设置设备
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"使用设备: {device}")
    
    # 加载配置
    with open("./config.json", 'r') as f:
        config = json.load(f)
    
    env_paras = config["env_paras"]
    model_paras = config["model_paras"]
    train_paras = config["train_paras"]
    
    env_paras["device"] = device
    model_paras["device"] = device
    
    # 计算模型输入维度
    model_paras["actor_in_dim"] = model_paras["out_size_ma"] * 2 + model_paras["out_size_ope"] * 2
    model_paras["critic_in_dim"] = model_paras["out_size_ma"] + model_paras["out_size_ope"]
    
    print(f"\n配置参数:")
    print(f"  作业数: {env_paras['num_jobs']}")
    print(f"  机器数: {env_paras['num_mas']}")
    print(f"  操作特征维度: {env_paras['ope_feat_dim']}")
    print(f"  机器特征维度: {env_paras['ma_feat_dim']}")
    print(f"  批大小: {env_paras['batch_size']}")
    
    # 初始化模型和记忆
    memories = PPO_model.Memory()
    model = PPO_model.PPO(model_paras, train_paras, num_envs=env_paras["batch_size"])
    
    # 创建训练数据生成器
    num_jobs = env_paras["num_jobs"]
    num_mas = env_paras["num_mas"]
    opes_per_job_min = int(num_mas * 0.8)
    opes_per_job_max = int(num_mas * 1.2)
    
    case_generator = CaseGenerator(num_jobs, num_mas, opes_per_job_min, opes_per_job_max)
    
    # 创建训练环境
    env_train_paras = copy.deepcopy(env_paras)
    env_train_paras["batch_size"] = env_paras["batch_size"]
    
    # 创建保存目录
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    save_path = f'./save/train_{timestamp}'
    os.makedirs(save_path, exist_ok=True)
    print(f"\n保存路径: {save_path}")
    
    # 训练循环
    best_makespan = float('inf')
    start_time = time.time()
    
    for iteration in range(train_paras["max_iterations"]):
        # 生成新的训练实例
        cases = case_generator.generate_case(env_paras["batch_size"])
        
        # 创建环境
        env = FJSPEnv(case=cases, env_paras=env_train_paras, data_source='generator')
        env.reset()
        
        # 收集轨迹
        states = []
        actions = []
        rewards = []
        dones = []
        
        while not env.done_batch.all():
            with torch.no_grad():
                state = env.state
                action = model.policy_old.act(state, memories, env.done_batch, flag_sample=True, flag_train=True)
            
            next_state, reward, done, _ = env.step(action)
            
            states.append(state)
            actions.append(action)
            rewards.append(reward)
            dones.append(done)
            
            # 检查是否需要更新
            if len(memories.rewards) >= train_paras["update_timestep"] * env_paras["batch_size"]:
                model.update(memories)
                memories.clear_memory()
        
        # 每N次迭代保存模型
        if (iteration + 1) % train_paras["save_timestep"] == 0:
            current_makespan = env.makespan_batch.mean().item()
            elapsed_time = time.time() - start_time
            
            print(f"\n迭代 {iteration + 1}/{train_paras['max_iterations']}")
            print(f"  平均完工时间: {current_makespan:.2f}")
            print(f"  已耗时: {elapsed_time:.2f}s")
            
            # 保存最佳模型
            if current_makespan < best_makespan:
                best_makespan = current_makespan
                model_path = f"{save_path}/model_best.pt"
                torch.save(model.policy.state_dict(), model_path)
                print(f"  ✓ 保存最佳模型: {model_path}")
            
            # 定期保存
            torch.save(model.policy.state_dict(), f"{save_path}/model_{iteration + 1}.pt")
        
        # 清理环境
        del env
    
    total_time = time.time() - start_time
    print(f"\n训练完成!")
    print(f"总耗时: {total_time:.2f}s")
    print(f"最佳完工时间: {best_makespan:.2f}")
    print(f"模型保存于: {save_path}")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
