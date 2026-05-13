#!/usr/bin/env python
"""
测试改进后的模型（启发式特征增强）
"""
import sys
import os
import json
import random
import time
import numpy as np
import torch

sys.path.insert(0, '.')

import PPO_model
from env.fjsp_env import FJSPEnv
from experiment_manager import ExperimentManager


def setup_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True


def main(data_path="1005", num_ins=10, num_average=10):
    SEED = 42
    setup_seed(SEED)
    
    # 创建实验管理器
    exp_manager = ExperimentManager(base_dir="experiment_results", 
                                   experiment_name=f"improved_heuristic_{data_path}")
    exp_manager.log("=" * 60)
    exp_manager.log(f"改进模型测试 (启发式特征增强)")
    exp_manager.log("=" * 60)
    
    # 设置设备
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    exp_manager.log(f"使用设备: {device}")
    
    # 加载配置
    with open("./config.json", 'r') as f:
        config = json.load(f)
    
    env_paras = config["env_paras"]
    model_paras = config["model_paras"]
    env_paras["device"] = device
    model_paras["device"] = device
    
    # 计算模型输入维度
    model_paras["actor_in_dim"] = model_paras["out_size_ma"] * 2 + model_paras["out_size_ope"] * 2
    model_paras["critic_in_dim"] = model_paras["out_size_ma"] + model_paras["out_size_ope"]
    
    exp_manager.log(f"\n配置参数:")
    exp_manager.log(f"  作业数: {env_paras['num_jobs']}")
    exp_manager.log(f"  机器数: {env_paras['num_mas']}")
    exp_manager.log(f"  操作特征维度: {env_paras['ope_feat_dim']}")
    exp_manager.log(f"  机器特征维度: {env_paras['ma_feat_dim']}")
    exp_manager.log(f"  测试实例数: {num_ins}")
    exp_manager.log(f"  每个实例运行次数: {num_average}")
    
    # 保存配置
    exp_manager.save_config(config, extra_info={
        "data_path": data_path,
        "num_ins": num_ins,
        "num_average": num_average,
        "seed": SEED,
        "improvements": ["启发式特征增强: 作业紧急程度", "启发式特征增强: 关键路径标记", 
                        "启发式特征增强: 机器负载", "启发式特征增强: 瓶颈机器标记"]
    })
    
    # 创建模型（使用新的特征维度）
    model = PPO_model.PPO(model_paras, config["train_paras"], num_envs=1)
    
    # 设置batch_size为1用于测试
    env_paras["batch_size"] = 1
    
    # 加载测试数据列表
    data_dir = f"./data_test/{data_path}/"
    file_list = sorted([f for f in os.listdir(data_dir) if f.endswith('.fjs')])[:num_ins]
    
    exp_manager.log(f"\n测试数据: {data_dir}")
    exp_manager.log(f"测试文件数: {len(file_list)}")
    
    # 存储结果
    all_makespans = []
    all_times = []
    details = []
    
    # 测试每个实例
    total_start_time = time.time()
    
    for idx, file_name in enumerate(file_list):
        file_path = os.path.join(data_dir, file_name)
        
        # 多次运行取平均
        makespans = []
        times = []
        
        for _ in range(num_average):
            # 创建环境 - 需要传递列表
            env = FJSPEnv(case=[file_path], env_paras=env_paras, data_source='file')
            state = env.reset()
            
            start_time = time.time()
            
            # 运行调度
            while not env.done_batch.all():
                with torch.no_grad():
                    action = model.policy_old.act(state, None, env.done_batch, 
                                                 flag_sample=False, flag_train=False)
                state, reward, done, _ = env.step(action)
            
            makespan = env.makespan_batch[0].item()
            elapsed = time.time() - start_time
            
            makespans.append(makespan)
            times.append(elapsed)
            
            del env
        
        # 计算平均值
        avg_makespan = np.mean(makespans)
        std_makespan = np.std(makespans)
        avg_time = np.mean(times)
        
        all_makespans.append(avg_makespan)
        all_times.append(avg_time)
        
        details.append({
            "file_name": file_name,
            "makespan": avg_makespan,
            "std": std_makespan,
            "time": avg_time
        })
        
        exp_manager.log(f"  [{idx+1}/{len(file_list)}] {file_name}: makespan={avg_makespan:.2f}±{std_makespan:.2f}, time={avg_time:.4f}s")
    
    # 计算总体统计
    overall_avg = np.mean(all_makespans)
    overall_std = np.std(all_makespans)
    overall_time = np.mean(all_times)
    total_time = time.time() - total_start_time
    
    exp_manager.log("\n" + "=" * 60)
    exp_manager.log(f"测试完成!")
    exp_manager.log(f"平均完工时间: {overall_avg:.2f} ± {overall_std:.2f}")
    exp_manager.log(f"平均计算时间: {overall_time:.4f}s")
    exp_manager.log(f"总耗时: {total_time:.2f}s")
    exp_manager.log("=" * 60)
    
    # 保存结果
    results = {
        "experiment_name": f"improved_heuristic_{data_path}",
        "timestamp": exp_manager.timestamp,
        "seed": SEED,
        "data_path": data_path,
        "num_ins": num_ins,
        "num_average": num_average,
        "avg_makespan": float(overall_avg),
        "std_makespan": float(overall_std),
        "avg_compute_time": float(overall_time),
        "total_time": float(total_time),
        "details": details,
        "config": config
    }
    
    exp_manager.save_results(results)
    
    return results


if __name__ == '__main__':
    data_path = sys.argv[1] if len(sys.argv) > 1 else "1005"
    num_ins = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    num_average = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    
    main(data_path, num_ins, num_average)
