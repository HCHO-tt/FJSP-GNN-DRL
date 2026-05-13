
# FJSP DRL 实验管理系统

这个系统用于运行和管理基于异构图神经网络 + PPO的柔性作业车间调度实验

## 文件结构

```
/workspace/
├── experiment_manager.py  # 实验管理核心模块
├── run_experiment.py     # 实验运行脚本
├── run_baseline.py       # 运行基线实验
├── configs/                 # 配置文件目录
│   ├── config_10_5.json
│   └── ...
└── experiment_results/  # 实验结果目录
    └── baseline_20260513_082559/
        ├── config.json
        ├── results.json
        ├── results.npy
        └── log.txt
```

## 实验管理器 (experiment_manager.py

核心模块提供以下功能：

1. **自动创建实验目录**：按时间戳自动创建独立的实验文件夹
2. **配置保存**：保存完整的实验配置和超参数
3. **日志记录**：记录实验过程和输出
4. **结果保存**：保存实验结果（JSON和NumPy格式）
5. **随机种子管理**：确保可重复性

## 使用方法

### 1. 快速开始

```python
from experiment_manager import ExperimentManager

# 创建实验管理器
with ExperimentManager(
    base_dir="experiment_results",
    experiment_name="my_experiment"
) as exp:
    # 记录日志
    exp.log("开始实验...")
    
    # 保存配置
    exp.save_config(config_dict, extra_info={"seed": 42})
    
    # 运行实验...
    
    # 保存结果
    exp.save_results(results_dict)
```

### 2. 运行基线实验

```bash
# 运行基线（原始论文实现
python run_baseline.py
```

### 3. 自定义实验

```python
from experiment_manager import ExperimentManager, setup_seed

def my_experiment():
    SEED = 42
    setup_seed(SEED)
    
    with ExperimentManager(experiment_name="improved_hgnn") as exp:
        # 加载和原始实验代码...
        pass

if __name__ == "__main__":
    my_experiment()
```

## 配置文件说明

### config.json (实验配置保存以下内容：

- **env_paras**: 环境参数
  - num_jobs, num_mas, batch_size, ...
- **model_paras**: 模型参数
  - 图神经网络维度、注意力头数...
- **train_paras**: 训练参数
  - 学习率、优化器参数...
- **test_paras**: 测试参数
  - 测试实例数量、采样参数...

## 实验结果目录

每个实验目录包含：

1. `config.json`: 完整实验配置（含随机种子）
2. `log.txt`: 实验过程日志
3. `results.json`: 易读的JSON格式结果
4. `results.npy`: NumPy格式结果（用于进一步分析）

## 运行原项目结构说明

原项目是以下论文的实现：
**"Flexible Job Shop Scheduling via Graph Neural Network and Deep Reinforcement Learning"**
发表于：IEEE Transactions on Industrial Informatics

## 改进建议

1. **架构改进：
   - 添加残差连接
   - 引入注意力机制优化
   - 元路径（Meta-path）机制

2. **强化学习改进：
   - 更先进的策略梯度算法
   - 奖励函数塑形
   - 多目标优化

3. **问题扩展：
   - 动态FJSP
   - 不确定性环境
   - 多目标优化
