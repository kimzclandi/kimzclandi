# kimzclandi

**简体中文** | [English](README.en.md)

[![Navigation](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml/badge.svg)](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml)

围绕小模型蒸馏与量化、Cache / Attention、性能分析和可复现数据流水线开展实验。各项目保留实现、固定配置、原始记录与失败分析，分别说明工程检查、模型质量与性能结论。

[项目状态与核验入口](docs/PROJECT_STATUS.md) · [名称与兼容性](docs/NAMING.md) · [公开仓库](https://github.com/kimzclandi?tab=repositories)

## 公开项目

按方向列出，不分主次；结果、限制与复现命令以各仓库默认分支为准。

### 推理、压缩与数据

- [inference-compression-lab](https://github.com/kimzclandi/inference-compression-lab)：大模型推理优化与性能分析。CPU 热路径、KV Cache、Attention 与 Metal 实验，均以原生框架作为对照；保留未通过速度门槛的负结果，没有 CUDA / Ascend 实测。
- [SmallModelQAFinetuningAndQuantization](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization)：小模型蒸馏与量化评测（两人合作）。Qwen 教师/学生的完整词表 logits 蒸馏、匹配 gold-SFT 对照与 MLX 量化；蒸馏未超过 gold-SFT，Q4 未通过质量门槛。
- [ChineseTextProcessingAndRetrieval](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval)：中文数据处理与检索。不可变快照、SQLite 血缘、Ray 恢复与 BM25 检索对照；切块收益伴随召回与耗时代价，当前规模下 Ray 慢于串行。

### 系统与 Agent

- [LeaseBasedShardScheduling](https://github.com/kimzclandi/LeaseBasedShardScheduling)：租约式分片调度与故障恢复。SQLite 租约、fencing、幂等提交；单机多进程，没有多 worker 加速证据。
- [AgentGate](https://github.com/kimzclandi/AgentGate)：Agent 工具调用的授权与审批（共同作者）。Go 实现参数绑定审批与审计，单实例原型。

### 视觉模型评测

- [ObjectDetectionDataSelection](https://github.com/kimzclandi/ObjectDetectionDataSelection)：目标检测数据选择与训练对照。BDD100K 小样本、仅训练 ROI 头；定向选样未稳定优于随机。
- [VLMImageDependenceEvaluation](https://github.com/kimzclandi/VLMImageDependenceEvaluation)：视觉语言模型图像依赖性评测。固定 SmolVLM，原图／空白／错配三种输入干预；只做推理评测，没有训练。

### 机器人与工业诊断

- [panda-obstacle-aware-posture-control](https://github.com/kimzclandi/panda-obstacle-aware-posture-control)：Panda 避障姿态控制。仿真中比较共享跟踪器下的势场与 PPO；PPO 复用上游实现，仅做仿真验证。
- [bearing-fault-diagnosis](https://github.com/kimzclandi/bearing-fault-diagnosis)：轴承故障诊断（合作项目）。CWRU 振动特征、稳健性评测与健康趋势分析；不做剩余寿命预测。

## 贡献与复现

代码、测试与文档使用 AI 辅助开发；各仓库分别说明个人实现、共同作者和上游框架归属。AI 辅助实现、框架提供的 kernel 与自主算法贡献分别标注。

主页只索引公开项目的默认分支材料。开发分支和未合并 PR 不作为已发布结果；实验原始失败与历史结论保留在对应仓库。CI 验证范围由工作流决定，绿色检查不表示模型质量、GPU 性能或业务部署通过。

本仓库仅维护导航。Python 3.10+，无需模型：

```sh
git clone https://github.com/kimzclandi/kimzclandi.git
cd kimzclandi
python3 -m unittest discover -s tests -v
python3 .github/scripts/check_docs.py
python3 scripts/verify_navigation.py
```

最后一项需网络，匿名读取公开仓库的默认分支 README 和链接文档；不会运行模型实验。

[贡献指南](CONTRIBUTING.md) · [行为准则](CODE_OF_CONDUCT.md) · [维护说明](docs/MAINTAINING.md)

## License

本主页仓库尚未指定许可证。各项目代码、数据和模型许可请以对应仓库为准。
