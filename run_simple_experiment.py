
#!/usr/bin/env python
"""
简化的基线实验运行脚本 - 无pandas依赖
"""
import sys
import os
import json
import time
import copy
import random
import numpy as np
from datetime import datetime


def setup_seed(seed):
    """设置随机种子"""
    import torch
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True


def create_experiment_dir(base_dir="experiment_results", experiment_name="baseline"):
    """创建实验目录"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    exp_dir = os.path.join(base_dir, f"{experiment_name}_{timestamp}")
    os.makedirs(exp_dir, exist_ok=True)
    return exp_dir, timestamp


def log_message(log_file, message):
    """记录日志"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    print(log_line)
    log_file.write(log_line + "\n")
    log_file.flush()


def main():
    print("=" * 60)
    print("FJSP DRL Project - Simple Baseline Experiment")
    print("=" * 60)
    
    # 创建实验目录
    exp_dir, timestamp = create_experiment_dir()
    log_path = os.path.join(exp_dir, "log.txt")
    config_path = os.path.join(exp_dir, "config.json")
    results_npy = os.path.join(exp_dir, "results.npy")
    results_json = os.path.join(exp_dir, "results.json")
    
    print(f"\nExperiment directory: {exp_dir}")
    
    with open(log_path, 'w', buffering=1) as log_file:
        log_message(log_file, "Starting baseline experiment...")
        
        # 设置随机种子
        SEED = 42
        setup_seed(SEED)
        log_message(log_file, f"Random seed set to: {SEED}")
        
        # 保存原始配置（先尝试快速测试配置）
        try:
            config_file = "config_quick_test.json" if os.path.exists("config_quick_test.json") else "config.json"
            with open(config_file, 'r') as f:
                config = json.load(f)
            
            full_config = {
                "experiment_name": "baseline",
                "timestamp": timestamp,
                "seed": SEED,
                "original_config": config
            }
            
            with open(config_path, 'w') as f:
                json.dump(full_config, f, indent=4)
            log_message(log_file, f"Configuration saved to: {config_path}")
        except Exception as e:
            log_message(log_file, f"Warning: Could not save config: {e}")
        
        # 导入项目模块
        log_message(log_file, "Importing project modules...")
        try:
            import torch
            import gym
            sys.path.insert(0, '.')
            
            from env.fjsp_env import FJSPEnv
            from env.load_data import nums_detec, load_fjs
            import PPO_model
        except Exception as e:
            log_message(log_file, f"Error importing modules: {e}")
            import traceback
            traceback.print_exc()
            return 1
        
        device = torch.device("cpu")
        torch.set_default_tensor_type('torch.FloatTensor')
        log_message(log_file, f"Using device: {device}")
        
        # 加载测试配置
        test_paras = config.get("test_paras", {})
        num_ins = test_paras.get("num_ins", 10)
        data_subdir = test_paras.get("data_path", "1005")
        num_average = test_paras.get("num_average", 10)
        
        data_path = os.path.join("data_test", data_subdir)
        if not os.path.exists(data_path):
            log_message(log_file, f"Error: Data path not found: {data_path}")
            return 1
        
        # 获取测试文件
        test_files = [f for f in os.listdir(data_path) if f.endswith('.fjs')]
        test_files.sort()
        test_files = test_files[:num_ins]
        log_message(log_file, f"Found {len(test_files)} test instances in {data_path}")
        
        # 加载模型
        model_path = os.path.join("model", "save_10_5.pt")
        if not os.path.exists(model_path):
            log_message(log_file, f"Error: Model file not found: {model_path}")
            return 1
        
        log_message(log_file, f"Loading model from: {model_path}")
        
        # 设置模型参数
        model_paras = config.get("model_paras", {})
        train_paras = config.get("train_paras", {})
        env_paras = config.get("env_paras", {})
        model_paras["device"] = device
        model_paras["actor_in_dim"] = model_paras.get("out_size_ma", 8) * 2 + model_paras.get("out_size_ope", 8) * 2
        model_paras["critic_in_dim"] = model_paras.get("out_size_ma", 8) + model_paras.get("out_size_ope", 8)
        
        # 初始化模型
        memories = PPO_model.Memory()
        model = PPO_model.PPO(model_paras, train_paras)
        
        try:
            model_CKPT = torch.load(model_path, map_location='cpu')
            model.policy.load_state_dict(model_CKPT)
            model.policy_old.load_state_dict(model_CKPT)
            log_message(log_file, "Model loaded successfully")
        except Exception as e:
            log_message(log_file, f"Error loading model: {e}")
            import traceback
            traceback.print_exc()
            return 1
        
        # 定义调度函数
        def schedule(env, model, memories):
            state = env.state
            dones = env.done_batch
            done = False
            start_time = time.time()
            while not done:
                with torch.no_grad():
                    actions = model.policy_old.act(state, memories, dones, flag_train=False)
                state, rewards, dones, _ = env.step(actions)
                done = dones.all()
            spend_time = time.time() - start_time
            
            gantt_result = env.validate_gantt()[0]
            if not gantt_result:
                log_message(log_file, "Warning: Scheduling validation failed!")
            return copy.deepcopy(env.makespan_batch), spend_time
        
        # 运行测试
        log_message(log_file, "Starting test on instances...")
        makespans = []
        times = []
        results_per_instance = []
        
        for idx, test_file in enumerate(test_files):
            file_path = os.path.join(data_path, test_file)
            log_message(log_file, f"[{idx+1}/{len(test_files)}] Testing: {test_file}")
            
            try:
                # 读取实例获取信息
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                num_jobs, num_mas, _ = nums_detec(lines)
                
                # 创建环境
                env_test_paras = copy.deepcopy(env_paras)
                env_test_paras["num_jobs"] = num_jobs
                env_test_paras["num_mas"] = num_mas
                env_test_paras["device"] = device
                
                env = gym.make('fjsp-v0', case=[file_path], env_paras=env_test_paras, data_source='file')
                env.reset()
                
                # 多次运行取平均
                instance_makespans = []
                instance_times = []
                
                for run in range(num_average):
                    makespan, t = schedule(env, model, memories)
                    instance_makespans.append(float(makespan))
                    instance_times.append(t)
                    env.reset()
                
                avg_makespan = float(np.mean(instance_makespans))
                avg_time = float(np.mean(instance_times))
                
                makespans.append(avg_makespan)
                times.append(avg_time)
                
                results_per_instance.append({
                    "instance": test_file,
                    "num_jobs": num_jobs,
                    "num_mas": num_mas,
                    "average_makespan": avg_makespan,
                    "average_compute_time": avg_time,
                    "all_makespans": instance_makespans
                })
                
                log_message(log_file, f"  Avg Makespan: {avg_makespan:.2f}, Avg Time: {avg_time:.4f}s")
                
            except Exception as e:
                log_message(log_file, f"Error testing {test_file}: {e}")
                import traceback
                traceback.print_exc()
        
        # 计算总体结果
        if makespans:
            avg_makespan_total = float(np.mean(makespans))
            std_makespan_total = float(np.std(makespans))
            avg_time_total = float(np.mean(times))
            
            log_message(log_file, "=" * 60)
            log_message(log_file, "EXPERIMENT SUMMARY")
            log_message(log_file, f"  Average Makespan: {avg_makespan_total:.2f} (±{std_makespan_total:.2f})")
            log_message(log_file, f"  Average Computation Time: {avg_time_total:.4f}s")
            log_message(log_file, "=" * 60)
            
            # 保存结果
            results = {
                "experiment_name": "baseline",
                "timestamp": timestamp,
                "seed": SEED,
                "results_per_instance": results_per_instance,
                "summary": {
                    "average_makespan": avg_makespan_total,
                    "std_makespan": std_makespan_total,
                    "average_compute_time": avg_time_total,
                    "all_makespans": makespans,
                    "all_compute_times": times
                }
            }
            
            # 保存为numpy和json
            np.save(results_npy, results, allow_pickle=True)
            log_message(log_file, f"Results saved to: {results_npy}")
            
            with open(results_json, 'w') as f:
                json.dump(results, f, indent=4, default=str)
            log_message(log_file, f"Results saved to: {results_json}")
            
            print(f"\n✅ Experiment completed successfully!")
            print(f"📁 Results in: {exp_dir}")
            
        else:
            log_message(log_file, "No results obtained!")
            return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
