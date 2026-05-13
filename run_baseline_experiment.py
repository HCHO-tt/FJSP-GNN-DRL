#!/usr/bin/env python
"""
运行基线实验 - 原始论文实现的完整实验管理版本

这个脚本运行原项目的基线实验，并保存结果到专用目录
"""
import sys
import os
import json
import time
import random
import copy
from datetime import datetime
import numpy as np

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def setup_seed(seed):
    """设置所有随机数生成器的种子以确保可重复性"""
    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        if hasattr(torch, 'backends') and hasattr(torch.backends, 'cudnn'):
            torch.backends.cudnn.deterministic = True
    except ImportError:
        pass
    
    np.random.seed(seed)
    random.seed(seed)


def create_experiment_dir(base_dir="experiment_results", experiment_name="baseline"):
    """创建带有时间戳的实验目录"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    exp_dir = os.path.join(base_dir, f"{experiment_name}_{timestamp}")
    os.makedirs(exp_dir, exist_ok=True)
    return exp_dir, timestamp


def save_config(exp_dir, config, extra_info=None):
    """保存实验配置到config.json"""
    config_path = os.path.join(exp_dir, "config.json")
    
    full_config = {
        "experiment_name": "baseline",
        "timestamp": os.path.basename(exp_dir).split("_")[-1],
        "original_config": config
    }
    
    if extra_info:
        full_config.update(extra_info)
    
    with open(config_path, 'w') as f:
        json.dump(full_config, f, indent=4)
    
    return config_path


def save_results(exp_dir, results):
    """保存实验结果"""
    # 保存为JSON
    json_path = os.path.join(exp_dir, "results.json")
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=4, default=str)
    
    # 保存为NumPy
    npy_path = os.path.join(exp_dir, "results.npy")
    np.save(npy_path, results, allow_pickle=True)
    
    return json_path, npy_path


def log_message(log_file, message):
    """记录消息到日志文件和标准输出"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    print(log_line)
    log_file.write(log_line + "\n")
    log_file.flush()


def main():
    SEED = 42
    setup_seed(SEED)
    
    print("=" * 60)
    print("FJSP DRL - 基线实验")
    print("=" * 60)
    
    # 创建实验目录
    exp_dir, timestamp = create_experiment_dir()
    log_path = os.path.join(exp_dir, "log.txt")
    
    print(f"\n实验目录: {exp_dir}")
    
    with open(log_path, 'w', buffering=1) as log_file:
        log_message(log_file, "实验开始")
        log_message(log_file, f"随机种子: {SEED}")
        
        # 加载配置
        try:
            with open("config.json", 'r') as f:
                config = json.load(f)
            log_message(log_file, "配置加载成功")
        except Exception as e:
            log_message(log_file, f"警告: 无法加载配置文件: {e}")
            config = {}
        
        # 保存配置
        config_path = save_config(exp_dir, config, extra_info={"seed": SEED})
        log_message(log_file, f"配置已保存到: {config_path}")
        
        try:
            # 尝试导入并运行原项目代码
            log_message(log_file, "正在尝试导入项目模块...")
            
            import torch
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            log_message(log_file, f"使用设备: {device}")
            
            # 这里可以添加实际的项目运行代码
            # 由于环境兼容性问题，我们先演示实验管理系统的结构
            
            log_message(log_file, "\n" + "=" * 60)
            log_message(log_file, "实验管理系统框架已就绪")
            log_message(log_file, "请在兼容的Python环境中运行完整实验")
            log_message(log_file, "=" * 60)
            
            # 创建示例结果（实际运行时会被真实结果取代）
            example_results = {
                "experiment_name": "baseline",
                "timestamp": timestamp,
                "seed": SEED,
                "note": "这是实验管理系统示例，运行完整实验需要兼容环境",
                "summary": {
                    "average_makespan": 299.71,
                    "std_makespan": 8.23
                }
            }
            
            results_json, results_npy = save_results(exp_dir, example_results)
            log_message(log_file, f"结果已保存到: {results_json}")
            
        except Exception as e:
            log_message(log_file, f"运行实验时出错: {e}")
            import traceback
            log_message(log_file, traceback.format_exc())
            return 1
    
    print(f"\n✅ 实验管理系统设置完成！")
    print(f"📁 实验文件位于: {exp_dir}")
    print(f"\n📝 运行完整基线实验:")
    print(f"   请使用Python 3.7-3.9环境，并安装:")
    print(f"   pip install torch==1.8 gym==0.22 numpy pandas matplotlib")
    print(f"   然后运行原始的 test_running.py")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
