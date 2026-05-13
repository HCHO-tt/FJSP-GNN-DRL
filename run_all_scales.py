#!/usr/bin/env python
"""
批量运行所有数据规模的实验
"""
import os
import subprocess
import sys

# 所有可用的数据规模
SCALES = [
    ("1005", 10, 10),   # 10 jobs × 5 machines
    ("1510", 10, 10),   # 15 jobs × 10 machines
    ("2005", 10, 10),   # 20 jobs × 5 machines
    ("2010", 10, 10),   # 20 jobs × 10 machines
    ("3010", 5, 5),     # 30 jobs × 10 machines (规模较大，减少测试数量)
    ("4010", 5, 5),     # 40 jobs × 10 machines (规模较大，减少测试数量)
]

def run_experiment(data_path, num_ins, num_average):
    """运行单个规模的实验"""
    print(f"\n{'='*60}")
    print(f"运行实验: {data_path} (实例数: {num_ins}, 平均次数: {num_average})")
    print(f"{'='*60}")
    
    cmd = [sys.executable, "run_experiment.py", data_path, str(num_ins), str(num_average)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    return result.returncode == 0

def main():
    print("批量运行所有数据规模的实验")
    print("="*60)
    
    success_count = 0
    total_count = len(SCALES)
    
    for data_path, num_ins, num_average in SCALES:
        if run_experiment(data_path, num_ins, num_average):
            success_count += 1
        print()
    
    print("="*60)
    print(f"批量实验完成: {success_count}/{total_count} 成功")
    print("="*60)
    
    return 0 if success_count == total_count else 1

if __name__ == '__main__':
    sys.exit(main())
