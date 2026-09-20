# kimzclandi · 数据工程与模型评测

[![CI](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml/badge.svg)](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml)

围绕数据加工与质量、工程可靠性、视觉模型评测及评测驱动的数据迭代开展实验。以下仓库提供可运行代码、逐条结果与复现说明；代码、测试和文档使用 AI 辅助开发，具体贡献与上游归属见各项目。

[项目状态与最小运行方式](docs/PROJECT_STATUS.md) · [全部公开仓库](https://github.com/kimzclandi?tab=repositories)

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

围绕小模型抽取式问答，记录 LoRA、响应蒸馏、数据覆盖与同框架量化。新增参考标签质量对照完成9次训练：同题修正目标在96题留出集上将平均严格EM从17.36%提高到24.31%，差值区间为[+1.04,+13.54]个百分点；使用了参考标签，不是无标注筛选收益。新增DRCD外部96题评测中，两组平均EM均为57.29%，差值区间[-5.21,+4.86]个百分点，未复现上述正向主比较。自动核验器失败、历史训练候选未通过采用门槛，以及Q8的限定质量保持结果均保留；未作业务部署验证。

[项目](https://github.com/kimzclandi/domain-qa-lab) · [运行](https://github.com/kimzclandi/domain-qa-lab/blob/main/docs/QUALITY_STUDY_RELEASE.md) · [质量对照与限制](https://github.com/kimzclandi/domain-qa-lab/blob/main/reports/quality-study-20260920/RESULTS.md) · [外部评测](https://github.com/kimzclandi/domain-qa-lab/blob/main/docs/EXTERNAL_DRCD.md)

### 5. AI Data Shard Lab · 可恢复的数据分片处理

将合成文本分片交给独立 HTTP worker，使用 SQLite 租约、递增 fencing token 与幂等提交处理重试和过期 worker。故障实验包含进程退出、协调器重启和提交确认丢失；确定性发布核对有效、重复与隔离记录的完整分母。范围是单机多进程，不代表多机生产系统或任务只执行一次。

[项目与运行](https://github.com/kimzclandi/ai-data-shard-lab) · [架构与语义](https://github.com/kimzclandi/ai-data-shard-lab/blob/main/docs/ARCHITECTURE.md) · [故障实验](https://github.com/kimzclandi/ai-data-shard-lab/blob/main/docs/RESULTS.md)

## 工程补充与配套研究

| 项目 | 独立问题与验证边界 |
|---|---|
| [Distill Quant Intent Lab](https://github.com/kimzclandi/distill-quant-intent-lab) | 8类意图的教师一致性筛选、三种子响应蒸馏与FP16/Q8/Q4对照；筛选未优于随机、绝对准确率偏低。保存数值导出故障、有限性门禁与修正证据。 |
| [AgentGate](https://github.com/kimzclandi/AgentGate) | Go 工具执行、资源授权、人工审批、幂等与撤销；单实例、内置业务资源。共同作者 [@kimzclandi](https://github.com/kimzclandi) 与 [@Lu-Ricardo-Y](https://github.com/Lu-Ricardo-Y)，外部集成与许可证状态见仓库。 |
| [Road Video Miner](https://github.com/kimzclandi/road-video-miner) | 已解码 KITTI 图像序列的片段选择与冗余分析；简单特征、等时间预算，无下游训练。 |
| [Detection Label Audit](https://github.com/kimzclandi/detection-label-audit) | 缓存检测预测上的合成污染排序与定位诊断；真实标签效用仍在研究中，59 图保留池未评分。 |

完整指标、负结果、数据许可与适用范围保留在各仓库。CI 的离线证据检查、实际推理与模型训练按项目分别说明。

[全部公开仓库](https://github.com/kimzclandi?tab=repositories)
