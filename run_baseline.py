
#!/usr/bin/env python
"""
简化的基线实验运行脚本
先测试基本功能是否正常
"""
import sys
import os


def check_project_structure():
    """检查项目结构是否完整"""
    print("Checking project structure...")
    
    required_files = [
        "config.json",
        "PPO_model.py", 
        "mlp.py",
        "env/fjsp_env.py",
        "env/load_data.py",
        "graph/hgnn.py",
        "model/save_10_5.pt"
    ]
    
    required_dirs = [
        "data_test",
        "model"
    ]
    
    all_good = True
    
    for f in required_files:
        if not os.path.exists(f):
            print(f"❌ Missing required file: {f}")
            all_good = False
        else:
            print(f"✅ Found: {f}")
    
    for d in required_dirs:
        if not os.path.isdir(d):
            print(f"❌ Missing required directory: {d}")
            all_good = False
        else:
            print(f"✅ Found directory: {d}")
    
    return all_good


def install_dependencies_simple():
    """尝试安装依赖"""
    print("\nInstalling dependencies...")
    import subprocess
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "torch", "numpy", "gym", "pandas", "matplotlib", "openpyxl"])
        print("✅ Dependencies installed successfully!")
        return True
    except Exception as e:
        print(f"⚠️ Could not install dependencies automatically: {e}")
        print("Please install them manually.")
        return False


def test_imports():
    """测试核心模块能否导入"""
    print("\nTesting imports...")
    try:
        import torch
        print(f"✅ PyTorch {torch.__version__} imported successfully")
    except Exception as e:
        print(f"❌ Failed to import PyTorch: {e}")
        return False
    
    try:
        import numpy as np
        print(f"✅ NumPy {np.__version__} imported successfully")
    except Exception as e:
        print(f"❌ Failed to import NumPy: {e}")
        return False
    
    try:
        import gym
        print(f"✅ Gym {gym.__version__} imported successfully")
    except Exception as e:
        print(f"❌ Failed to import Gym: {e}")
        return False
    
    try:
        import pandas as pd
        print(f"✅ Pandas {pd.__version__} imported successfully")
    except Exception as e:
        print(f"⚠️ Pandas not available (not critical for testing): {e}")
    
    print("\nTrying to import project modules...")
    try:
        sys.path.insert(0, '.')
        from env.load_data import nums_detec
        print("✅ env.load_data.nums_detec imported successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to import project modules: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    print("=" * 60)
    print("FJSP DRL Project - Baseline Setup")
    print("=" * 60)
    
    # 检查项目结构
    if not check_project_structure():
        print("\n❌ Project structure incomplete!")
        return 1
    
    # 尝试安装依赖
    # install_dependencies_simple()  # 可选安装
    
    # 测试导入
    if not test_imports():
        print("\n❌ Failed to import required modules!")
        return 1
    
    print("\n" + "=" * 60)
    print("Basic checks passed!")
    print("\nNext steps:")
    print("1. Make sure all dependencies are installed")
    print("2. Run 'python experiment_manager.py' to execute full baseline experiment")
    print("=" * 60)
    
    # 询问是否直接运行实验
    try:
        response = input("\nDo you want to run the baseline experiment now? (y/n): ")
        if response.lower().strip() in ['y', 'yes']:
            print("\nStarting baseline experiment...")
            from experiment_manager import run_baseline_experiment
            run_baseline_experiment()
    except KeyboardInterrupt:
        print("\nExperiment cancelled by user.")
    except Exception as e:
        print(f"\nError running experiment: {e}")
        import traceback
        traceback.print_exc()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
