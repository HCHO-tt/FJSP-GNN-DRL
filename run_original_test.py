
#!/usr/bin/env python
"""
基于原始test_running.py的完整实验管理版本
"""
import copy
import json
import os
import random
import time
import numpy as np
from datetime import datetime

import gym
import torch
import PPO_model
from env.fjsp_env import FJSPEnv
from env.load_data import nums_detec


def setup_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True


def create_experiment_manager(base_dir="experiment_results", experiment_name="baseline"):
    """简单的实验管理"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    exp_dir = os.path.join(base_dir, f"{experiment_name}_{timestamp}")
    os.makedirs(exp_dir, exist_ok=True)
    return exp_dir, timestamp


def log_to_file(file_path, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    print(log_line)
    with open(file_path, 'a', buffering=1) as f:
        f.write(log_line + "\n")


def schedule(env, model, memories, flag_sample=False):
    state = env.state
    dones = env.done_batch
    done = False
    last_time = time.time()
    while not done:
        with torch.no_grad():
            actions = model.policy_old.act(state, memories, dones, flag_sample=flag_sample, flag_train=False)
        state, rewards, dones, _ = env.step(actions)
        done = dones.all()
    spend_time = time.time() - last_time
    
    gantt_result = env.validate_gantt()[0]
    if not gantt_result:
        print("Scheduling Error!")
    return copy.deepcopy(env.makespan_batch), spend_time


def main():
    print("=" * 60)
    print("FJSP DRL Baseline Experiment")
    print("=" * 60)
    
    # 实验设置
    SEED = 42
    setup_seed(SEED)
    
    # 创建实验目录
    exp_dir, timestamp = create_experiment_manager()
    log_path = os.path.join(exp_dir, "log.txt")
    config_path = os.path.join(exp_dir, "config.json")
    results_path = os.path.join(exp_dir, "results.json")
    
    print(f"\nExperiment directory: {exp_dir}")
    log_to_file(log_path, "Experiment started")
    log_to_file(log_path, f"Random seed: {SEED}")
    
    # 保存原始配置
    try:
        with open("config.json", 'r') as f:
            original_config = json.load(f)
        
        exp_config = {
            "experiment_name": "baseline",
            "timestamp": timestamp,
            "seed": SEED,
            "original_config": original_config
        }
        
        with open(config_path, 'w') as f:
            json.dump(exp_config, f, indent=4)
        log_to_file(log_path, f"Configuration saved to {config_path}")
    except Exception as e:
        log_to_file(log_path, f"Warning: Could not save config: {e}")
    
    # 环境设置
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    if device.type == 'cuda':
        torch.cuda.set_device(device)
        torch.set_default_tensor_type('torch.cuda.FloatTensor')
    else:
        torch.set_default_tensor_type('torch.FloatTensor')
    log_to_file(log_path, f"Using device: {device}")
    
    # 加载配置
    with open("config.json", 'r') as load_f:
        load_dict = json.load(load_f)
    env_paras = load_dict["env_paras"]
    model_paras = load_dict["model_paras"]
    train_paras = load_dict["train_paras"]
    test_paras = load_dict["test_paras"]
    
    # 为了快速测试，我们修改参数
    test_paras["num_ins"] = 2
    test_paras["num_average"] = 2
    
    env_paras["device"] = device
    model_paras["device"] = device
    env_test_paras = copy.deepcopy(env_paras)
    num_ins = test_paras["num_ins"]
    
    if test_paras["sample"]:
        env_test_paras["batch_size"] = test_paras["num_sample"]
    else:
        env_test_paras["batch_size"] = 1
    model_paras["actor_in_dim"] = model_paras["out_size_ma"] * 2 + model_paras["out_size_ope"] * 2
    model_paras["critic_in_dim"] = model_paras["out_size_ma"] + model_paras["out_size_ope"]
    
    data_path = "./data_test/{0}/".format(test_paras["data_path"])
    test_files = os.listdir(data_path)
    test_files.sort(key=lambda x: x[:-4])
    test_files = test_files[:num_ins]
    
    log_to_file(log_path, f"Testing on {len(test_files)} instances from {data_path}")
    
    # 加载模型
    memories = PPO_model.Memory()
    model = PPO_model.PPO(model_paras, train_paras)
    
    # 检查并加载模型
    model_files = [f for f in os.listdir('./model/') if f.endswith('.pt')]
    if not model_files:
        log_to_file(log_path, "Error: No model files found!")
        return 1
    
    model_file = model_files[0]
    model_path = f"./model/{model_file}"
    log_to_file(log_path, f"Loading model: {model_file}")
    
    if device.type == 'cuda':
        model_CKPT = torch.load(model_path)
    else:
        model_CKPT = torch.load(model_path, map_location='cpu')
    
    model.policy.load_state_dict(model_CKPT)
    model.policy_old.load_state_dict(model_CKPT)
    log_to_file(log_path, "Model loaded successfully")
    
    # 运行测试
    log_to_file(log_path, "Starting tests...")
    envs = []
    all_makespans = []
    all_times = []
    results_per_instance = []
    
    start_time = time.time()
    
    for i_ins in range(num_ins):
        test_file = data_path + test_files[i_ins]
        log_to_file(log_path, f"Processing instance {i_ins+1}/{num_ins}: {test_files[i_ins]}")
        
        with open(test_file) as file_object:
            line = file_object.readlines()
            ins_num_jobs, ins_num_mas, _ = nums_detec(line)
        
        env_test_paras["num_jobs"] = ins_num_jobs
        env_test_paras["num_mas"] = ins_num_mas
        
        if len(envs) == num_ins:
            env = envs[i_ins]
        else:
            # 直接实例化环境，避免gym的兼容性检查问题
            from env.fjsp_env import FJSPEnv
            env = FJSPEnv(case=[test_file], env_paras=env_test_paras, data_source='file')
            env.reset()
            envs.append(copy.deepcopy(env))
            log_to_file(log_path, f"Created environment {i_ins}")
        
        time_s = []
        makespan_s = []
        
        for j in range(test_paras["num_average"]):
            makespan, time_re = schedule(env, model, memories)
            makespan_s.append(float(makespan))
            time_s.append(float(time_re))
            env.reset()
        
        avg_makespan = float(np.mean(makespan_s))
        avg_time = float(np.mean(time_s))
        all_makespans.append(avg_makespan)
        all_times.append(avg_time)
        
        results_per_instance.append({
            "instance": test_files[i_ins],
            "num_jobs": ins_num_jobs,
            "num_mas": ins_num_mas,
            "average_makespan": avg_makespan,
            "average_time": avg_time,
            "all_makespans": makespan_s,
            "all_times": time_s
        })
        
        log_to_file(log_path, f"  Instance {i_ins+1}: Avg Makespan = {avg_makespan:.2f}, Avg Time = {avg_time:.4f}s")
    
    total_time = time.time() - start_time
    
    # 总结结果
    avg_makespan_total = float(np.mean(all_makespans))
    std_makespan_total = float(np.std(all_makespans))
    avg_time_total = float(np.mean(all_times))
    
    log_to_file(log_path, "=" * 60)
    log_to_file(log_path, "EXPERIMENT SUMMARY")
    log_to_file(log_path, f"  Average Makespan: {avg_makespan_total:.2f} (±{std_makespan_total:.2f})")
    log_to_file(log_path, f"  Average Computation Time: {avg_time_total:.4f}s")
    log_to_file(log_path, f"  Total Time: {total_time:.2f}s")
    log_to_file(log_path, "=" * 60)
    
    # 保存结果
    results = {
        "experiment_name": "baseline",
        "timestamp": timestamp,
        "seed": SEED,
        "results_per_instance": results_per_instance,
        "summary": {
            "average_makespan": avg_makespan_total,
            "std_makespan": std_makespan_total,
            "average_time": avg_time_total,
            "total_time": total_time,
            "all_makespans": all_makespans,
            "all_times": all_times
        }
    }
    
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=4, default=str)
    
    log_to_file(log_path, f"Results saved to {results_path}")
    
    print(f"\n✅ Experiment completed!")
    print(f"📁 Results in: {exp_dir}")
    
    return 0


if __name__ == "__main__":
    main()
