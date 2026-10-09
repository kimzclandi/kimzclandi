# kimzclandi

**简体中文** | [English](README.en.md)

![模型推理、压缩与数据工程](.github/project-header.svg)

[![Navigation](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml/badge.svg)](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml)

围绕小模型蒸馏与量化、Cache / Attention、性能分析和可复现数据流水线开展实验。各项目保留实现、固定配置、原始记录与失败分析，分别说明工程检查、模型质量与性能结论。

[项目状态与核验入口](docs/PROJECT_STATUS.md) · [名称与兼容性](docs/NAMING.md) · [公开仓库](https://github.com/kimzclandi?tab=repositories)

## 核心项目

### 01 · 大模型推理优化与性能分析

[inference-compression-lab](https://github.com/kimzclandi/inference-compression-lab) · Python / ONNX Runtime / MLX / Metal

CPU 热路径剪枝、Cache 实验与 Attention 数值检查，使用原生框架控制组分析优化空间。固定 M4 Max CPU 负载下，包含排序与拒答的热请求计算由 **68.681 → 55.342 ms**；`load_service` 初始化由 **17.919 → 5.139 s**，后者不含进程启动和请求推理。

保留负结果：Metal residual-add + RMSNorm 相对编译原生路径慢约 **23.8%**；真实 Qwen 原生 Cache 容量预留未通过加速门槛。Mac 记录不代表 CUDA / Ascend 实测或生产服务收益。

[热路径实现与记录](https://github.com/kimzclandi/inference-compression-lab/blob/codex/research-prerelease/docs/qa-risk-pruning.md) · [初始化](https://github.com/kimzclandi/inference-compression-lab/blob/codex/research-prerelease/docs/qa-risk-startup.md) · [Attention](https://github.com/kimzclandi/inference-compression-lab/blob/codex/research-prerelease/docs/attention-backend-study.md) · [原生 Cache 对照](https://github.com/kimzclandi/inference-compression-lab/blob/codex/research-prerelease/docs/qwen-cache-reservation.md) · [Metal 负结果](https://github.com/kimzclandi/inference-compression-lab/blob/codex/research-prerelease/docs/metal-residual-rmsnorm.md)

### 02 · 小模型蒸馏与量化评测

[SmallModelQAFinetuningAndQuantization](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization) · PyTorch / LoRA / 完整词表 KL / MLX

固定 Qwen 教师与学生，构建回答 token 的完整词表 logits 缓存、CE + 温度 KL 训练及匹配 gold-SFT 控制组。v2 使用 **242 条 TRAIN、3 seeds × 242 步**；74 题 dev 归一化 EM 为 **60.36% ± 2.81%**，低于 gold-SFT 的 **64.86% ± 1.35%**，未证明 soft targets 带来质量优势（3 seeds 均值 ± 样本标准差）。

量化记录分别报告权重体积、推理耗时和逐题质量；保留 Q4 质量失败、历史响应蒸馏及外部评估。dev 已复用，不能当作独立质量确认。模型与量化基础能力来自上游框架。

[训练与数据协议](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization/blob/main/docs/LOGITS_DISTILLATION_V2.md) · [逐题结果与控制组](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization/blob/main/reports/logits-distillation-v2/RESULTS.md) · [代码与证据索引](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization/blob/main/docs/EVIDENCE_MAP.md) · [贡献边界](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization/blob/main/CONTRIBUTIONS.md)

## 辅助项目

### 03 · 中文数据处理与检索

[ChineseTextProcessingAndRetrieval](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval) · Ray / SQLite / BM25

对 **2,403 篇文段、10,142 个候选问题**实施质量检查、不可变快照、血缘与失败恢复。重叠切块将留出集 span-hit@3 从 **81.25% → 89.38%**，同时文档 recall@3 从 **95.625% → 95.00%**、块数增加 **40.14%**、查询中位耗时由 **7.50 → 12.04 ms**。当前规模 Ray 慢于 serial。

后续 PreparedBM25 在固定同次对照中约 **1.86–1.87×**，640 个 query-index 对、1,920 个分数精确一致；额外索引状态为 O(V+N)。这项查询优化与上述切块质量实验分开记录。

[运行](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval/blob/main/docs/REPRODUCE.md) · [检索结果与代价](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval/blob/main/reports/RESULTS.md) · [查询优化](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval/blob/main/docs/BM25_EXACT_OPTIMIZATION.md) · [恢复与一致性](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval/blob/main/docs/EVIDENCE_MAP.md)

## 系统与 Agent 工程

| 项目 | 问题与范围 | 直接核验 |
|---|---|---|
| [租约式分片调度与故障恢复](https://github.com/kimzclandi/LeaseBasedShardScheduling) | SQLite 租约、fencing、幂等提交；单机多进程，未证明多 worker 加速。 | [实现与运行](https://github.com/kimzclandi/LeaseBasedShardScheduling#readme) |
| [AgentGate](https://github.com/kimzclandi/AgentGate) | Go 工具授权、参数绑定审批与审计；共同作者项目、单实例原型。 | [架构](https://github.com/kimzclandi/AgentGate/blob/main/docs/ARCHITECTURE.md) · [测试与限制](https://github.com/kimzclandi/AgentGate/blob/main/docs/TEST_REPORT.md) |

## 视觉模型评测

| 项目 | 问题与范围 | 直接核验 |
|---|---|---|
| [目标检测数据选择与训练对照](https://github.com/kimzclandi/ObjectDetectionDataSelection) | BDD100K 小样本、ROI 头训练；定向选样未稳定优于随机。 | [训练对照](https://github.com/kimzclandi/ObjectDetectionDataSelection/blob/main/docs/FAILURE_V2_REPORT.md) |
| [视觉语言模型图像依赖性评测](https://github.com/kimzclandi/VLMImageDependenceEvaluation) | 固定 SmolVLM、90 题 × 三种视觉输入干预；推理评测，无训练收益。 | [运行](https://github.com/kimzclandi/VLMImageDependenceEvaluation/blob/main/docs/RUNNING.md) · [干预结果](https://github.com/kimzclandi/VLMImageDependenceEvaluation/blob/main/docs/GROUNDING_V3_REPORT.md) |

## 机器人与工业诊断

| 项目 | 问题与范围 | 直接核验 |
|---|---|---|
| [Panda 避障姿态控制](https://github.com/kimzclandi/panda-obstacle-aware-posture-control) | 仿真项目：共享跟踪器下的势场与 PPO 对照、500 回合仿真评估；PPO 复用上游实现。 | [在线解读](https://github.com/kimzclandi/panda-obstacle-aware-posture-control/blob/main/deliverables/final_20261009/interpretation_zh.md) · [完整包复现说明](https://github.com/kimzclandi/panda-obstacle-aware-posture-control/blob/main/docs/reproduction.md) |
| [轴承故障诊断](https://github.com/kimzclandi/bearing-fault-diagnosis) | 合作项目：CWRU 振动特征、稳健性评测与健康趋势分析；不作为剩余寿命预测。 | [实验报告](https://github.com/kimzclandi/bearing-fault-diagnosis/blob/main/outputs/full-verified/reports/experiment.md) · [保存证据复核](https://github.com/kimzclandi/bearing-fault-diagnosis/blob/main/outputs/full-verified/reports/verification.json) |

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
