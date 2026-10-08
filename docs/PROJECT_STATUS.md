# 项目状态与核验入口

本索引只使用公开默认分支材料。离线回算、数据流水线重跑、模型推理、训练与性能重测是不同操作；绿色 CI 只表示对应检查通过。运行前按链接仓库 README 准备环境，不把保存证据复核称为新实验。

| 项目 | 已实现内容 | 当前边界 | 核验入口 |
|---|---|---|---|
| [大模型推理优化与性能分析](https://github.com/kimzclandi/inference-compression-lab) | CPU 热路径、Cache、Attention 数值检查、Metal 实验与原始失败 | Metal 慢于原生；原生 Cache 预留未达加速门槛；无 CUDA / Ascend 实测 | README 安装与离线验证命令；`experiments.verify_qa_risk_pruning`、`experiments.verify_qa_risk_startup`；真实运行另需匹配硬件和模型 |
| [小模型蒸馏与量化评测](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization) | 完整词表 logits 蒸馏、匹配 gold-SFT、缓存/模型身份预检、MLX 量化 | v2 dev 低于 gold-SFT；复用 dev 不构成独立确认；Q4 质量失败 | `scripts/acceptance.py` 运行测试和离线证据验证，不下载模型、不训练或重新推理 |
| [中文数据处理与检索](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval) | 不可变资产、血缘、Ray 恢复、BM25 与逐题证据 | span 收益伴随召回退化和成本；当前规模 Ray 更慢 | `scripts/verify.py`、`scripts/verify_portable.py`；`scripts/reproduce_portable.py` 在新目录重建 |
| [租约式分片调度与故障恢复](https://github.com/kimzclandi/LeaseBasedShardScheduling) | SQLite 租约、fencing、幂等提交与故障实验 | 单机多进程；无多 worker 加速证据，不是任务只执行一次 | 标准库测试与 `scripts/verify_evidence.py` |
| [AgentGate](https://github.com/kimzclandi/AgentGate) | 工具授权、参数绑定审批与 SQLite 审计 | 共同作者、单实例原型 | README 中 Go 测试与演示入口 |
| [目标检测数据选择与训练对照](https://github.com/kimzclandi/ObjectDetectionDataSelection) | 固定预算、多 seed、ROI 头训练与失败切片 | 小样本；定向选择未稳定优于随机 | `scripts/verify_artifacts.py`；模型重跑另需数据 |
| [视觉语言模型图像依赖性评测](https://github.com/kimzclandi/VLMImageDependenceEvaluation) | 合成图像三种干预与逐条预测 | 固定模型推理，无训练收益 | `scripts/verify_grounding.py` |
| [Panda 避障姿态控制](https://github.com/kimzclandi/panda-obstacle-aware-posture-control) | 共享跟踪器下的势场/PPO 控制及仿真 | 仿真范围，以仓库协议为准 | README 评估入口与保存结果 |
| [轴承故障诊断](https://github.com/kimzclandi/bearing-fault-diagnosis) | 振动特征、稳健性与健康趋势 | 工业诊断方向，以仓库协议为准 | README 的数据准备、训练与评估入口 |

## Publication boundary

Linked default branches contain the summarized evidence. Unmerged pull requests are separate development work. This index does not claim independent quality confirmation, production service readiness, target-device acceleration, or personal mastery from passing CI.
