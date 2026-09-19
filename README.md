# kimzclandi · 数据工程与模型评测

[![CI](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml/badge.svg)](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml)

围绕数据加工与质量、工程可靠性、视觉模型评测及评测驱动的数据迭代开展实验。以下仓库提供可运行代码、逐条结果与复现说明；代码、测试和文档使用 AI 辅助开发，具体贡献与上游归属见各项目。

## 主要项目

### 1. Chinese Evidence Data Engine · 可追溯的中文数据加工

将公开中文文段转为可检查的数据资产：质量算子、Ray 任务、内容寻址缓存、原子快照与 SQLite 血缘，并用检索失败分析比较切块方法。保存了串行/Ray 一致性、故障恢复和逐题检索结果；重叠切块改善证据覆盖，同时增加索引与查询成本。当前为单机小语料实验，没有 Ray 加速证据。

[项目](https://github.com/kimzclandi/chinese-evidence-data-engine) · [运行](https://github.com/kimzclandi/chinese-evidence-data-engine/blob/main/docs/REPRODUCE.md) · [结果](https://github.com/kimzclandi/chinese-evidence-data-engine/blob/main/reports/RESULTS.md)

### 2. Driving Data Engine · 固定预算下的检测数据选择

在 BDD100K 小样本上比较随机与定向选样，仅微调预训练检测器的 ROI 预测头。提供三种子、匹配训练步数的对照、失败切片及排序机制诊断；当前未证明定向选择稳定优于随机。Ray 扩展仅在单机验证。

[项目与运行](https://github.com/kimzclandi/driving-data-engine) · [训练对照](https://github.com/kimzclandi/driving-data-engine/blob/main/docs/FAILURE_V2_REPORT.md) · [机制诊断](https://github.com/kimzclandi/driving-data-engine/blob/main/docs/DIAGNOSIS_V3_REPORT.md)

### 3. VLM Data Flywheel Lab · 视觉输入干预与失败分析

固定 SmolVLM，对合成场景执行原图、空白图和错配图干预，保存 90 题 × 三种输入、共 270 次真实生成与配对切片结果。观察到的视觉贡献主要来自空间题；这是推理评测，没有模型训练收益。历史 metadata 规则演示与真实推理分开记录。

[项目](https://github.com/kimzclandi/vlm-data-flywheel-lab) · [运行](https://github.com/kimzclandi/vlm-data-flywheel-lab/blob/main/docs/RUNNING.md) · [干预结果](https://github.com/kimzclandi/vlm-data-flywheel-lab/blob/main/docs/GROUNDING_V3_REPORT.md)

### 4. Domain QA Lab · 数据覆盖、训练与量化对照

围绕小模型抽取式问答，记录 LoRA、响应蒸馏、数据覆盖、同框架量化与中文新来源验证。训练候选未通过采用门槛；Q8 在限定的英文开发集与中文样本中通过质量保持检查，不能据此推断业务可用。五轮逐条预测、拒答基线和失败案例可核验。

[项目](https://github.com/kimzclandi/domain-qa-lab) · [运行](https://github.com/kimzclandi/domain-qa-lab/blob/main/docs/REPRODUCE_CLOSURE.md) · [中文验证](https://github.com/kimzclandi/domain-qa-lab/blob/main/reports/chinese-v5/RESULTS.md)

## 工程补充与配套研究

| 项目 | 独立问题与验证边界 |
|---|---|
| [AgentGate](https://github.com/kimzclandi/AgentGate) | Go 工具执行、资源授权、人工审批、幂等与撤销；单实例、内置业务资源。共同作者 [@kimzclandi](https://github.com/kimzclandi) 与 [@Lu-Ricardo-Y](https://github.com/Lu-Ricardo-Y)，外部集成与许可证状态见仓库。 |
| [AI Data Shard Lab](https://github.com/kimzclandi/ai-data-shard-lab) | HTTP worker 的租约、fencing、幂等提交与进程故障恢复；单机合成文本实验。 |
| [Road Video Miner](https://github.com/kimzclandi/road-video-miner) | 已解码 KITTI 图像序列的片段选择与冗余分析；简单特征、等时间预算，无下游训练。 |
| [Detection Label Audit](https://github.com/kimzclandi/detection-label-audit) | 缓存检测预测上的合成污染排序与定位诊断；真实标签效用仍在研究中，59 图保留池未评分。 |

完整指标、负结果、数据许可与适用范围保留在各仓库。CI 的离线证据检查、实际推理与模型训练按项目分别说明。

[全部公开仓库](https://github.com/kimzclandi?tab=repositories)
