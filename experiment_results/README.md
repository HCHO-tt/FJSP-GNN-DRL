
# 实验结果目录

此目录包含所有实验运行结果，结构如下：

```
experiment_results/
├── README.md
└── baseline_20260513_082559/  # 示例基线实验
    ├── config.json
    ├── log.txt
    ├── results.json
    └── results.npy
```

## 命名规则

实验目录名称格式：`{experiment_name}_{timestamp}`

- `experiment_name`: 实验名称
- `timestamp`: 时间戳 (YYYYMMDD_HHMMSS)

## 基线实验 (baseline)

基线实验使用原始论文的实现：

- **模型**: HGNN (异构图神经网络) + PPO
- **作者**: Song et al.
- **论文**: "Flexible Job Shop Scheduling via Graph Neural Network and Deep Reinforcement Learning"
- **发表**: IEEE Transactions on Industrial Informatics

## 如何运行新实验

参见 `/workspace/experiments/README.md` 获取完整指南。
