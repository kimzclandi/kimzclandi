# kimzclandi · AI 数据处理与模型评测

[![CI](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml/badge.svg)](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml)

这里记录 AI 数据处理、模型评测和数据选择实验。每个仓库提供输入、实现、运行命令、保存结果与限制。代码、测试和文档使用 AI 辅助开发；单机实验、模型推理、模型训练和生产部署分别说明。

## 从这里开始

| 主题 | 仓库 | 可检查的内容 |
|---|---|---|
| 数据处理可靠性 | [ai-data-shard-lab](https://github.com/kimzclandi/ai-data-shard-lab) | HTTP 多进程 worker、租约、幂等提交、故障恢复和数据清单；单机合成数据 |
| 模型评测 | [vlm-data-flywheel-lab](https://github.com/kimzclandi/vlm-data-flywheel-lab) | 270 次真实 SmolVLM 推理、视觉输入干预与切片评测；无训练 |
| 数据选择 | [driving-data-engine](https://github.com/kimzclandi/driving-data-engine) | 固定预算、三种子与匹配训练步数的检测器预测头微调；保留负结果 |

## 数据处理可靠性实验

[ai-data-shard-lab](https://github.com/kimzclandi/ai-data-shard-lab) · 2026-09-18 开始

Python HTTP 协调器与独立 worker 进程完成文本数据分片处理，SQLite 持久化租约、attempt token、提交结果和事件。实现过期重试、旧 token 拒绝、重复提交重放、异常数据隔离、精确去重和来源哈希清单。

本地实验使用 1,200 行合成文本、24 个分片；单 worker、四 worker 和故障注入共 7 次运行生成相同 manifest。27 项测试通过。真实进程故障覆盖 worker 中断与协调器重启；**单机四 worker 没有观察到加速，不代表多机生产经验或模型收益**。

[三分钟运行](https://github.com/kimzclandi/ai-data-shard-lab#readme) · [实验报告](https://github.com/kimzclandi/ai-data-shard-lab/blob/main/docs/RESULTS.md) · [架构](https://github.com/kimzclandi/ai-data-shard-lab/blob/main/docs/ARCHITECTURE.md) · [代码审查路径](https://github.com/kimzclandi/ai-data-shard-lab/blob/main/docs/REVIEW.md)

## 模型评测与视觉输入干预

[vlm-data-flywheel-lab](https://github.com/kimzclandi/vlm-data-flywheel-lab)

固定 SmolVLM-256M，对合成图像执行原图、空白、错配输入下的真实推理。保留集三任务宏平均为 **54.7% / 40.0% / 25.3%**；全部45题准确率分别为 **44.4% / 33.3% / 22.2%**。视觉贡献主要来自空间题，未训练模型，不能外推通用 grounding 或真机能力。历史 metadata 规则演示单独保留。

[中文介绍与运行](https://github.com/kimzclandi/vlm-data-flywheel-lab/blob/main/README.zh-CN.md) · [视觉干预报告](https://github.com/kimzclandi/vlm-data-flywheel-lab/blob/main/docs/GROUNDING_V3_REPORT.md)

## 数据选择与训练对照

[driving-data-engine](https://github.com/kimzclandi/driving-data-engine)

在 BDD100K 小样本上比较选样方法，只微调预训练检测器的 ROI 预测头。最新三种子、等112步对照中，定向−随机为 **−0.634 AP 点**，区间 [−1.631, +0.323]，未证明稳定优势。后续开发集诊断分析排序为何缺少区分力；Ray 等扩展仅为单机实验。

[当前结果与运行](https://github.com/kimzclandi/driving-data-engine#readme) · [训练报告](https://github.com/kimzclandi/driving-data-engine/blob/main/docs/FAILURE_V2_REPORT.md) · [机制诊断](https://github.com/kimzclandi/driving-data-engine/blob/main/docs/DIAGNOSIS_V3_REPORT.md)

## 配套研究

### 道路序列片段选择与冗余分析

[road-video-miner](https://github.com/kimzclandi/road-video-miner)

处理 KITTI PNG 序列，以相同片段时间预算比较均匀时间、外观去重和时序覆盖。时序相对随机的参考漏检轨迹覆盖差为 **+6.95 个百分点**，区间 [−7.32, +20.89]，未证明稳定优势；没有下游训练收益。跨平台回放验证历史选择及指标，不保证位级相同名单。

[实验报告](https://github.com/kimzclandi/road-video-miner/blob/main/docs/REPORT.md) · [运行与边界](https://github.com/kimzclandi/road-video-miner/blob/main/docs/PROTOCOL_AND_REPRODUCE.md)

### 检测标签复核排序与错误定位诊断

[detection-label-audit](https://github.com/kimzclandi/detection-label-audit)

复用上游检测预测，没有新增训练或推理。开发集合成污染的三次×8图预算中，原组合选中11次污染图、6次严格定位、3次定位证据达到最高分；guard对应 **17、12、7次**。两方法全范围可定位的16个(seed, image)集合相同，当前收益主要是排序清理。

**70.83%是开发集合成污染的图级命中率，不是真实标签效果或定位准确率。** 旧40图只有探索性批量反馈；59图保留池未评分，仍缺少独立真实裁决。

[定位诊断](https://github.com/kimzclandi/detection-label-audit/blob/main/docs/LOCALIZATION_V4.md) · [运行说明](https://github.com/kimzclandi/detection-label-audit/blob/main/docs/REPRODUCE.md)

## AgentGate

[AgentGate](https://github.com/kimzclandi/AgentGate) · 共同作者：[@kimzclandi](https://github.com/kimzclandi) 与 [@Lu-Ricardo-Y](https://github.com/Lu-Ricardo-Y)

基于 Go 的多租户 Agent 身份与工具执行平台，支持文档访问、工单处理、受限委托、资源授权、人工审批、幂等和权限撤销，配有运行管理与审计控制台。

文档与工单使用 SQLite 持久化，提供确定性本地模式和可配置的模型接口。当前采用单实例、内置工具架构；外部模型与 OIDC 集成状态见项目文档。

[快速开始](https://github.com/kimzclandi/AgentGate#readme) · [架构](https://github.com/kimzclandi/AgentGate/blob/main/docs/ARCHITECTURE.md) · [API](https://github.com/kimzclandi/AgentGate/blob/main/docs/API.md)


---

这是个人研究项目与合作工程项目的导航，不是额外技术项目。各结果受数据规模与实验设计限制；各仓库的实验与部署范围以项目说明为准。[全部仓库](https://github.com/kimzclandi?tab=repositories)
