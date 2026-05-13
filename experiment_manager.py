
import os
import json
import time
import numpy as np
from datetime import datetime


class ExperimentManager:
    """实验管理类，负责创建实验文件夹、保存配置、记录日志等"""
    
    def __init__(self, base_dir="experiment_results", experiment_name="baseline"):
        self.base_dir = base_dir
        self.experiment_name = experiment_name
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.experiment_dir = os.path.join(base_dir, f"{experiment_name}_{self.timestamp}")
        self.config_path = os.path.join(self.experiment_dir, "config.json")
        self.results_path = os.path.join(self.experiment_dir, "results.npy")
        self.log_path = os.path.join(self.experiment_dir, "log.txt")
        
        # 创建实验目录
        os.makedirs(self.experiment_dir, exist_ok=True)
        
        # 初始化日志文件
        self.log_file = open(self.log_path, 'w', buffering=1)
        self.log(f"Experiment started at {self.timestamp}")
    
    def log(self, message):
        """记录日志到文件和标准输出"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] {message}"
        print(log_line)
        self.log_file.write(log_line + "\n")
    
    def save_config(self, config_dict, extra_info=None):
        """保存配置文件"""
        config_copy = json.loads(json.dumps(config_dict, default=str))
        
        full_config = {
            "experiment_name": self.experiment_name,
            "timestamp": self.timestamp,
            "config": config_copy
        }
        
        if extra_info:
            full_config.update(extra_info)
        
        with open(self.config_path, 'w') as f:
            json.dump(full_config, f, indent=4)
        
        self.log(f"Configuration saved to {self.config_path}")
        return full_config
    
    def save_results(self, results_dict):
        """保存实验结果"""
        np.save(self.results_path, results_dict, allow_pickle=True)
        self.log(f"Results saved to {self.results_path}")
    
    def close(self):
        """关闭实验管理器"""
        self.log(f"Experiment completed")
        self.log_file.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.log(f"Error occurred: {exc_type.__name__}: {exc_val}")
        self.close()
        return False


def run_baseline_experiment():
    """运行基线实验的完整流程"""
    import copy
    import json
    import random
    import time
    
    import gym
    import torch
    import numpy as np
    import PPO_model
    from env.fjsp_env import FJSPEnv
    from env.load_data import nums_detec
    
    def setup_seed(seed):
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        np.random.seed(seed)
        random.seed(seed)
        torch.backends.cudnn.deterministic = True
    
    # 设置随机种子
    SEED = 42
    setup_seed(SEED)
    
    # 创建实验管理器
    with ExperimentManager(experiment_name="baseline") as exp:
        exp.log("=" * 60)
        exp.log("Starting Baseline Experiment")
        exp.log("=" * 60)
        
        # 加载配置
        with open("./config.json", 'r') as load_f:
            load_dict = json.load(load_f)
        
        # 保存原始配置和实验信息
        extra_info = {
            "seed": SEED,
            "random_seed_info": {
                "torch": torch.initial_seed(),
                "numpy": np.random.get_state()[1][0] if hasattr(np.random, 'get_state') else None,
            }
        }
        exp.save_config(load_dict, extra_info)
        
        # 设备设置
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        exp.log(f"Using device: {device}")
        
        if device.type == 'cuda':
            torch.cuda.set_device(device)
            torch.set_default_tensor_type('torch.cuda.FloatTensor')
        else:
            torch.set_default_tensor_type('torch.FloatTensor')
        
        # 解析配置
        env_paras = load_dict["env_paras"]
        model_paras = load_dict["model_paras"]
        train_paras = load_dict["train_paras"]
        test_paras = load_dict["test_paras"]
        
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
        
        exp.log(f"Environment parameters: {env_paras}")
        exp.log(f"Model parameters: {model_paras}")
        
        # 加载测试数据
        data_path = "./data_test/{0}/".format(test_paras["data_path"])
        test_files = os.listdir(data_path)
        test_files.sort(key=lambda x: x[:-4])
        test_files = test_files[:num_ins]
        
        exp.log(f"Testing on {len(test_files)} instances from {data_path}")
        
        # 加载模型
        memories = PPO_model.Memory()
        model = PPO_model.PPO(model_paras, train_paras)
        
        mod_files = os.listdir('./model/')
        model_files = [f for f in mod_files if f.endswith('.pt')]
        
        if not model_files:
            exp.log("Error: No model files found in ./model/!")
            return
        
        # 选择第一个模型文件
        model_file = model_files[0]
        exp.log(f"Loading model: {model_file}")
        
        if device.type == 'cuda':
            model_CKPT = torch.load('./model/' + model_file)
        else:
            model_CKPT = torch.load('./model/' + model_file, map_location='cpu')
        
        model.policy.load_state_dict(model_CKPT)
        model.policy_old.load_state_dict(model_CKPT)
        
        # 定义调度函数
        def schedule(env, model, memories, flag_sample=False):
            state = env.state
            dones = env.done_batch
            done = False
            i = 0
            start_time = time.time()
            while ~done:
                i += 1
                with torch.no_grad():
                    actions = model.policy_old.act(state, memories, dones, flag_sample=flag_sample, flag_train=False)
                state, rewards, dones, _ = env.step(actions)
                done = dones.all()
            spend_time = time.time() - start_time
            
            gantt_result = env.validate_gantt()[0]
            if not gantt_result:
                exp.log("WARNING: Scheduling Error!")
            return copy.deepcopy(env.makespan_batch), spend_time
        
        # 运行测试
        exp.log("Starting testing...")
        makespans = []
        times = []
        envs = []
        results_per_instance = []
        
        for i_ins in range(num_ins):
            test_file = data_path + test_files[i_ins]
            exp.log(f"Processing instance {i_ins+1}/{num_ins}: {test_files[i_ins]}")
            
            with open(test_file) as file_object:
                line = file_object.readlines()
                ins_num_jobs, ins_num_mas, _ = nums_detec(line)
            
            env_test_paras["num_jobs"] = ins_num_jobs
            env_test_paras["num_mas"] = ins_num_mas
            
            if len(envs) == num_ins:
                env = envs[i_ins]
            else:
                env = gym.make('fjsp-v0', case=[test_file], env_paras=env_test_paras, data_source='file')
                env.reset()
                envs.append(copy.deepcopy(env))
            
            time_s = []
            makespan_s = []
            
            for j in range(test_paras["num_average"]):
                makespan, time_re = schedule(env, model, memories)
                makespan_s.append(makespan)
                time_s.append(time_re)
                env.reset()
            
            avg_makespan = float(torch.mean(torch.tensor(makespan_s)))
            avg_time = float(torch.mean(torch.tensor(time_s)))
            
            makespans.append(avg_makespan)
            times.append(avg_time)
            
            results_per_instance.append({
                "instance": test_files[i_ins],
                "num_jobs": ins_num_jobs,
                "num_mas": ins_num_mas,
                "makespan": avg_makespan,
                "computation_time": avg_time,
                "all_makespans": [float(m) for m in makespan_s]
            })
            
            exp.log(f"  Instance {i_ins+1} - Avg Makespan: {avg_makespan:.2f}, Avg Time: {avg_time:.4f}s")
        
        # 计算总体统计
        avg_makespan_total = float(np.mean(makespans))
        std_makespan_total = float(np.std(makespans))
        avg_time_total = float(np.mean(times))
        
        exp.log("=" * 60)
        exp.log("Experiment Summary:")
        exp.log(f"  Average Makespan: {avg_makespan_total:.2f} (±{std_makespan_total:.2f})")
        exp.log(f"  Average Computation Time: {avg_time_total:.4f}s")
        exp.log("=" * 60)
        
        # 保存结果
        results = {
            "experiment_name": exp.experiment_name,
            "timestamp": exp.timestamp,
            "config": load_dict,
            "seed": SEED,
            "results_per_instance": results_per_instance,
            "summary": {
                "avg_makespan": avg_makespan_total,
                "std_makespan": std_makespan_total,
                "avg_computation_time": avg_time_total,
                "all_makespans": makespans,
                "all_computation_times": times
            }
        }
        
        exp.save_results(results)
        
        # 同时保存为易读的 JSON 格式
        results_json_path = os.path.join(exp.experiment_dir, "results.json")
        with open(results_json_path, 'w') as f:
            json.dump(results, f, indent=4)
        exp.log(f"Results also saved to {results_json_path}")
        
        return results


if __name__ == "__main__":
    run_baseline_experiment()
