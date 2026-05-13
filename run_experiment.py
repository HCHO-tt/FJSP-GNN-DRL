#!/usr/bin/env python
"""
灵活的实验运行脚本 - 支持多种数据规模
"""
import sys
import os
import json
import random
import copy
import time
from datetime import datetime
import numpy as np
import pandas as pd
import torch

sys.path.insert(0, '.')

from env.fjsp_env import FJSPEnv
import PPO_model
from env.load_data import nums_detec


def setup_seed(seed):
    """设置所有随机数生成器的种子以确保可重复性"""
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True


def create_experiment_dir(base_dir="experiment_results", experiment_name="baseline"):
    """创建带有时间戳的实验目录"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    exp_dir = os.path.join(base_dir, f"{experiment_name}_{timestamp}")
    os.makedirs(exp_dir, exist_ok=True)
    return exp_dir, timestamp


def log_message(log_file, message):
    """记录消息到日志文件和标准输出"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    print(log_line)
    log_file.write(log_line + "\n")
    log_file.flush()


def schedule(env, model, memories, flag_sample=False):
    """执行调度"""
    state = env.state
    dones = env.done_batch
    done = False
    last_time = time.time()
    i = 0
    while not done:
        i += 1
        with torch.no_grad():
            actions = model.policy_old.act(state, memories, dones, flag_sample=flag_sample, flag_train=False)
        state, rewards, dones, _ = env.step(actions)
        done = dones.all()
    spend_time = time.time() - last_time

    gantt_result = env.validate_gantt()[0]
    if not gantt_result:
        print("Scheduling Error！！！！！！")
    return copy.deepcopy(env.makespan_batch), spend_time


def main(data_path="1005", num_ins=10, num_average=10):
    SEED = 42
    setup_seed(SEED)
    
    print("=" * 60)
    print(f"FJSP DRL - 实验 (规模: {data_path})")
    print("=" * 60)
    
    # 创建实验目录
    exp_dir, timestamp = create_experiment_dir(experiment_name=f"baseline_{data_path}")
    log_path = os.path.join(exp_dir, "log.txt")
    
    with open(log_path, 'w', buffering=1) as log_file:
        log_message(log_file, "实验开始")
        log_message(log_file, f"随机种子: {SEED}")
        log_message(log_file, f"数据规模: {data_path}")
        
        # 加载配置
        with open("./config.json", 'r') as load_f:
            load_dict = json.load(load_f)
        env_paras = load_dict["env_paras"]
        model_paras = load_dict["model_paras"]
        train_paras = load_dict["train_paras"]
        test_paras = load_dict["test_paras"]
        
        # 更新测试参数
        test_paras["data_path"] = data_path
        test_paras["num_ins"] = num_ins
        test_paras["num_average"] = num_average
        
        log_message(log_file, "配置加载成功")
        
        # 保存配置
        config_path = os.path.join(exp_dir, "config.json")
        env_paras_save = env_paras.copy()
        model_paras_save = model_paras.copy()
        
        with open(config_path, 'w') as f:
            json.dump({
                "experiment_name": f"baseline_{data_path}",
                "timestamp": timestamp,
                "seed": SEED,
                "data_scale": data_path,
                "env_paras": env_paras_save,
                "model_paras": model_paras_save,
                "train_paras": train_paras,
                "test_paras": test_paras
            }, f, indent=4)
        log_message(log_file, f"配置已保存到: {config_path}")
        
        # 设置设备
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        log_message(log_file, f"使用设备: {device}")
        
        env_paras["device"] = device
        model_paras["device"] = device
        env_test_paras = copy.deepcopy(env_paras)
        
        # 设置模型参数
        model_paras["actor_in_dim"] = model_paras["out_size_ma"] * 2 + model_paras["out_size_ope"] * 2
        model_paras["critic_in_dim"] = model_paras["out_size_ma"] + model_paras["out_size_ope"]
        
        # 获取测试文件
        data_folder = f"./data_test/{data_path}/"
        test_files = os.listdir(data_folder)
        test_files.sort(key=lambda x: x[:-4])
        test_files = test_files[:num_ins]
        
        log_message(log_file, f"测试数据: {data_folder}")
        log_message(log_file, f"测试实例数: {len(test_files)}")
        
        # 初始化模型
        memories = PPO_model.Memory()
        model = PPO_model.PPO(model_paras, train_paras)
        
        # 加载预训练模型 - 根据规模选择
        model_dir = './model/'
        mod_files = [f for f in os.listdir(model_dir) if f.endswith('.pt')]
        
        # 尝试找到匹配规模的模型
        target_model = None
        for mf in mod_files:
            if data_path[:2] in mf or data_path in mf:
                target_model = mf
                break
        
        if not target_model and mod_files:
            target_model = mod_files[0]
        
        if target_model:
            log_message(log_file, f"加载模型: {target_model}")
            model_CKPT = torch.load(model_dir + target_model, map_location=device)
            model.policy.load_state_dict(model_CKPT)
            model.policy_old.load_state_dict(model_CKPT)
        else:
            log_message(log_file, "警告: 未找到预训练模型")
            return 1
        
        # 运行测试
        log_message(log_file, "开始测试...")
        makespans = []
        times = []
        file_names = []
        
        start_total = time.time()
        for i_ins, test_file in enumerate(test_files):
            file_path = data_folder + test_file
            file_names.append(test_file)
            
            log_message(log_file, f"处理实例 {i_ins+1}/{len(test_files)}: {test_file}")
            
            # 读取实例信息
            with open(file_path) as file_object:
                lines = file_object.readlines()
                ins_num_jobs, ins_num_mas, _ = nums_detec(lines)
            
            env_test_paras["num_jobs"] = ins_num_jobs
            env_test_paras["num_mas"] = ins_num_mas
            env_test_paras["batch_size"] = 1
            
            # 创建环境
            env = FJSPEnv(case=[file_path], env_paras=env_test_paras, data_source='file')
            env.reset()
            
            # 运行调度
            time_s = []
            makespan_s = []
            for j in range(num_average):
                makespan, time_re = schedule(env, model, memories)
                makespan_s.append(makespan.item())
                time_s.append(time_re)
                env.reset()
            
            makespans.append(np.mean(makespan_s))
            times.append(np.mean(time_s))
            
            log_message(log_file, f"  Makespan: {makespans[-1]:.2f}, Time: {times[-1]:.4f}s")
        
        total_time = time.time() - start_total
        log_message(log_file, f"测试完成，总耗时: {total_time:.2f}s")
        
        # 计算统计结果
        avg_makespan = np.mean(makespans)
        std_makespan = np.std(makespans)
        avg_time = np.mean(times)
        
        log_message(log_file, f"平均完工时间: {avg_makespan:.2f} ± {std_makespan:.2f}")
        log_message(log_file, f"平均计算时间: {avg_time:.4f}s")
        
        # 保存结果
        env_paras_save["device"] = str(env_paras["device"])
        model_paras_save["device"] = str(model_paras["device"])
        
        results = {
            "experiment_name": f"baseline_{data_path}",
            "timestamp": timestamp,
            "seed": SEED,
            "device": str(device),
            "data_scale": data_path,
            "test_instances": len(test_files),
            "num_average": num_average,
            "avg_makespan": float(avg_makespan),
            "std_makespan": float(std_makespan),
            "avg_compute_time": float(avg_time),
            "total_time": float(total_time),
            "details": {
                "file_names": file_names,
                "makespans": [float(m) for m in makespans],
                "times": [float(t) for t in times]
            },
            "config": {
                "env_paras": env_paras_save,
                "model_paras": model_paras_save,
                "test_paras": test_paras
            }
        }
        
        # 保存JSON
        json_path = os.path.join(exp_dir, "results.json")
        with open(json_path, 'w') as f:
            json.dump(results, f, indent=4)
        
        # 保存NumPy
        npy_path = os.path.join(exp_dir, "results.npy")
        np.save(npy_path, results)
        
        # 保存Excel
        df = pd.DataFrame({
            "file_name": file_names,
            "makespan": makespans,
            "time": times
        })
        df.to_excel(os.path.join(exp_dir, "results.xlsx"), index=False)
        
        log_message(log_file, f"结果已保存到: {exp_dir}")
        log_message(log_file, "实验结束")
    
    print(f"\n✅ 实验完成！")
    print(f"📁 实验文件位于: {exp_dir}")
    print(f"📊 数据规模: {data_path}")
    print(f"📊 平均完工时间: {avg_makespan:.2f} ± {std_makespan:.2f}")
    print(f"⏱️  平均计算时间: {avg_time:.4f}s")
    
    return 0


if __name__ == '__main__':
    # 解析命令行参数
    data_path = "1005"
    num_ins = 10
    num_average = 10
    
    if len(sys.argv) > 1:
        data_path = sys.argv[1]
    if len(sys.argv) > 2:
        num_ins = int(sys.argv[2])
    if len(sys.argv) > 3:
        num_average = int(sys.argv[3])
    
    sys.exit(main(data_path, num_ins, num_average))
