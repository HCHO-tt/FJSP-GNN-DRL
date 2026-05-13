#!/usr/bin/env python
"""
简单的环境测试脚本
"""
import sys
import os
sys.path.insert(0, '.')

import json
import torch
from env.fjsp_env import FJSPEnv
from env.load_data import nums_detec

print("Testing FJSP Environment...")

# 加载配置
with open("config.json", 'r') as f:
    config = json.load(f)

env_paras = config["env_paras"]
env_paras["device"] = torch.device("cpu")
env_paras["batch_size"] = 1

# 获取测试文件
data_path = "./data_test/1005/"
test_files = [f for f in os.listdir(data_path) if f.endswith('.fjs')][:1]
test_file = data_path + test_files[0]

print(f"Testing with: {test_file}")

# 读取实例
with open(test_file, 'r') as f:
    lines = f.readlines()

num_jobs, num_mas, _ = nums_detec(lines)
print(f"Instance: {num_jobs} jobs, {num_mas} machines")

env_paras["num_jobs"] = num_jobs
env_paras["num_mas"] = num_mas

# 创建环境
try:
    env = FJSPEnv(case=[test_file], env_paras=env_paras, data_source='file')
    print("✅ Environment created successfully!")
    
    print(f"\nEnvironment state:")
    print(f"  num_opes: {env.num_opes}")
    print(f"  state.feat_opes_batch shape: {env.state.feat_opes_batch.shape}")
    print(f"  state.feat_mas_batch shape: {env.state.feat_mas_batch.shape}")
    print(f"  state.proc_times_batch shape: {env.state.proc_times_batch.shape}")
    print(f"  state.ope_ma_adj_batch shape: {env.state.ope_ma_adj_batch.shape}")
    
    # 测试reset
    env.reset()
    print("\n✅ Reset successful!")
    
except Exception as e:
    print(f"❌ Error creating environment: {e}")
    import traceback
    traceback.print_exc()
