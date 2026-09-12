# kimzclandi · 个人实验与项目

[![CI](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml/badge.svg)](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml)

这里记录我在目标检测、视觉模型评测和数据选择上的个人实验。主项目是小样本检测数据选择，另外包含视觉输入干预、道路片段选择和标签复核三个专题。各仓库提供代码、运行说明、实验结果和限制；代码、测试与文档使用 AI 辅助开发。

## 合作工程项目：AgentGate

[AgentGate](https://github.com/kimzclandi/AgentGate) · 共同制作：[@kimzclandi](https://github.com/kimzclandi) 与 [@Lu-Ricardo-Y](https://github.com/Lu-Ricardo-Y)

Go 多租户 Agent 安全执行平台：文档与工单统一资源授权、受限委托、参数绑定人工审批、持久幂等与撤销，以及连接真实后端的管理控制台。提供 20 个顶层 Go 测试、race/vet 检查和 22 项固定 HTTP 验收证据；这些是确定性回归结果，不是真实模型通用成功率。

默认 mock，数据库读写真实执行；可选模型和 OIDC 适配尚无外部凭证实测，不宣称生产 IAM 或通用代码沙箱。代码与文档使用 AI 辅助开发，个人分工不作虚构。

[运行与架构](https://github.com/kimzclandi/AgentGate#readme) · [测试与性能报告](https://github.com/kimzclandi/AgentGate/blob/main/docs/TEST_REPORT.md) · [面试讲解](https://github.com/kimzclandi/AgentGate/blob/main/docs/INTERVIEW.md)

## 主项目：小样本目标检测数据选择

[driving-data-engine](https://github.com/kimzclandi/driving-data-engine)

在 BDD100K 小样本上比较选样方法，只微调预训练检测器的 ROI 预测头。最新三种子、等112步对照中，定向−随机为 **−0.634 AP 点**，区间 [−1.631, +0.323]，未证明稳定优势。后续开发集诊断分析排序为何缺少区分力；Ray 等扩展仅为单机实验。

[当前结果与运行](https://github.com/kimzclandi/driving-data-engine#readme) · [训练报告](https://github.com/kimzclandi/driving-data-engine/blob/main/docs/FAILURE_V2_REPORT.md) · [机制诊断](https://github.com/kimzclandi/driving-data-engine/blob/main/docs/DIAGNOSIS_V3_REPORT.md)

## 第二专题：小型 VLM 的视觉输入干预

[vlm-data-flywheel-lab](https://github.com/kimzclandi/vlm-data-flywheel-lab)

固定 SmolVLM-256M，对合成图像执行原图、空白、错配输入下的真实推理。保留集三任务宏平均为 **54.7% / 40.0% / 25.3%**；全部45题准确率分别为 **44.4% / 33.3% / 22.2%**。视觉贡献主要来自空间题，未训练模型，不能外推通用 grounding 或真机能力。历史 metadata 规则演示单独保留。

[中文介绍与运行](https://github.com/kimzclandi/vlm-data-flywheel-lab/blob/main/README.zh-CN.md) · [视觉干预报告](https://github.com/kimzclandi/vlm-data-flywheel-lab/blob/main/docs/GROUNDING_V3_REPORT.md)

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

---

这是个人研究项目与合作工程项目的导航，不是额外技术项目。结果均受各自数据与实验设计限制，未声称生产部署或机器人实测成果。[全部仓库](https://github.com/kimzclandi?tab=repositories)
