# kimzclandi · 项目导航

**AI 数据与评测 · 自动驾驶 · 机器人与具身智能**

AI Data & Evaluation · Autonomous Driving · Robotics & Embodied AI

这里按方向整理我的公开项目，方便查看代码、运行方法和实验依据。核心链路是：识别失败 → 数据假设 → 固定预算策略 → 受控验证 → 依据证据继续或拒绝。代码由 AI 辅助完成；所有成果区分真实运行、合成控制与未验证边界。

[AI 数据与评测](#ai-data) · [自动驾驶](#autonomous-driving) · [机器人与具身智能](#robotics) · [全部仓库](https://github.com/kimzclandi?tab=repositories)

---

<a id="ai-data"></a>
## 01 · AI 数据与模型评测

### [Embodied VLM Data Flywheel Lab](https://github.com/kimzclandi/vlm-data-flywheel-lab)

把模型失败转化为可审查的数据生产计划，并通过固定测试集检查版本退化。

`合成数据 → 评测 → 失败分析 → 样本优先级 → 针对性增强 → 回归门禁`

| 查看维度 | 项目内容 |
|---|---|
| 关注问题 | 如何选择值得生产的数据，以及如何避免总体分数掩盖能力退化 |
| 实际产物 | 保留 240 条规则样本与 108 条历史增强；保留第一轮72题/144次生成；新增90题/30场景族、270次真实/空白/错配干预 |
| 展示能力 | 图像输入隔离、场景族切分、配对实验、失败分母、开发集挖掘与数据血缘 |
| 技术栈 | Python · PyTorch · Transformers · Pillow · Streamlit · pytest · GitHub Actions |
| 验证边界 | 真实 SmolVLM CPU 推理 + 独立规则历史；无模型训练、真机实验或训练收益 |

**从这里开始：** [中文介绍与启动](https://github.com/kimzclandi/vlm-data-flywheel-lab/blob/main/README.zh-CN.md) · [实际实验报告](https://github.com/kimzclandi/vlm-data-flywheel-lab/blob/main/docs/GROUNDING_V3_REPORT.md) · [数据策略](https://github.com/kimzclandi/vlm-data-flywheel-lab/blob/main/docs/DATA_STRATEGY.md) · [核心代码](https://github.com/kimzclandi/vlm-data-flywheel-lab/tree/main/src/flywheel) · [CI 状态](https://github.com/kimzclandi/vlm-data-flywheel-lab/actions)

> 第一轮真实 VLM 提示比较未超过先验；新平衡实验的保留集任务宏平均为真实54.7%、空白40.0%、错配25.3%，有限视觉贡献主要来自空间题，不外推通用推理。历史规则候选总体提高但计数退化，被 REJECT；这些都不是训练收益。

<a id="autonomous-driving"></a>
## 02 · 自动驾驶

### [Driving Data Engine · 道路长尾数据闭环](https://github.com/kimzclandi/driving-data-engine)

在固定数据预算下比较采样策略，用真实检测头训练和可恢复的数据流程检验结果。

`真实道路图像 → 质量检查 → 模型推理 → 样本筛选 → 实际微调 → 切片评测与回归`

| 查看维度 | 项目内容 |
|---|---|
| 关注问题 | 哪些道路图像值得进入训练，怎样区分数据收益与额外训练的影响 |
| 实际产物 | 保留240图旧实验；新增120张评测图，定向/随机/seed-only × 三seed，统一112步 |
| 真实 VLM | SmolVLM 昼夜标签实验，比较自由生成与有限标签解码，保留格式错误和语义分歧 |
| 数据工程 | 来源与版本追踪、Parquet/DuckDB、SQLite 幂等恢复、单机 Ray Data 一致性与吞吐实验 |
| 技术栈 | Python · PyTorch · Transformers · Ray Data · DuckDB · Streamlit · pytest · GitHub Actions |
| 验证边界 | 仅微调检测器 ROI 预测头；公开数据小规模实验；新实验定向−随机为−0.634 AP点，区间跨零；无人工降本或PB级处理证据 |

**从这里开始：** [启动与结果](https://github.com/kimzclandi/driving-data-engine#readme) · [实际实验报告](https://github.com/kimzclandi/driving-data-engine/blob/main/docs/FAILURE_V2_REPORT.md) · [VLM 质检](https://github.com/kimzclandi/driving-data-engine/blob/main/docs/VLM_QUALITY.md) · [岗位能力与证据](https://github.com/kimzclandi/driving-data-engine/blob/main/docs/CAPABILITY_EVIDENCE_V2.md) · [CI 状态](https://github.com/kimzclandi/driving-data-engine/actions)

[新增开发集机制诊断](https://github.com/kimzclandi/driving-data-engine/blob/main/docs/DIAGNOSIS_V3_REPORT.md)：完整评分与低分质量项秩相关0.988，留组原型AUC0.395，不再追加缺乏依据的同类训练。

> 项目保留了不支持预期的结果：不确定性采样未稳定优于随机组，小规模 Ray 扫描慢于串行；VLM 输出格式合法也不保证语义正确。每项结论均有配置和原始报告可核查。

### [Road Video Miner · 视频场景挖掘](https://github.com/kimzclandi/road-video-miner)

20个KITTI序列、120个不重叠片段、600帧真实CPU推理；按每序列相同两秒预算比较随机、均匀时间、外观去重和时序覆盖，使用参考漏检轨迹做序列级评价。

- **新增能力：** 帧—片段—序列血缘，时间预算，序列隔离，参考失败覆盖与冗余分别评价。
- **实际结论：** 时序相对随机+6.95个百分点，序列区间[−7.32,+20.89]，不支持稳定优势；没有下游模型训练。
- **工程边界：** PNG序列而非视频容器解码；跨平台存在近同分选择差异，公开CI验证原始选择的贪心条件和指标回放，不声称位级相同选择。

[实际报告](https://github.com/kimzclandi/road-video-miner/blob/main/docs/REPORT.md) · [复现与协议](https://github.com/kimzclandi/road-video-miner/blob/main/docs/PROTOCOL_AND_REPRODUCE.md) · [面试与核心函数](https://github.com/kimzclandi/road-video-miner/blob/main/docs/INTERVIEW.md) · [CI](https://github.com/kimzclandi/road-video-miner/actions)

### [Detection Label Audit · 检测标签质量审计](https://github.com/kimzclandi/detection-label-audit)

真实道路参考框与固定检测输出上的五类可控污染实验：漏标、类别错、框尺度错、重复与坐标管线错误；比较随机、几何规则和模型一致性，保留原始标签待复核队列。

- **新增能力：** 问题候选与真值分离、固定复核预算、分类型召回、模型错误与标签错误的裁决边界。
- **实际结论：** 12图预算下几何/组合方法均为100%合成污染命中率、20%总召回，仅覆盖易识别重复/坐标错误，未证明模型项增量收益。
- **验证边界：** 100%不代表真实标签效果；86张原始图有线索但全部待人工复核。无新增神经推理、自动修复或训练收益。原区间计算被拒绝并保留，另有预算保持统计修复。

[实际报告](https://github.com/kimzclandi/detection-label-audit/blob/main/docs/REPORT.md) · [复现](https://github.com/kimzclandi/detection-label-audit/blob/main/docs/REPRODUCE.md) · [岗位与面试](https://github.com/kimzclandi/detection-label-audit/blob/main/docs/INTERVIEW.md) · [CI](https://github.com/kimzclandi/detection-label-audit/actions)

<a id="robotics"></a>
## 03 · 机器人与具身智能

**目前暂无该分类的独立公开项目。**

后续项目可围绕机械臂操作、标定、机器人学习和系统工具组织。现有 VLM 数据项目涉及具身场景，主分类放在“AI 数据与模型评测”。

---

### 如何浏览

- **了解项目价值：**先读项目介绍与实际实验报告。
- **运行与复现：**进入各项目仓库，使用其独立的安装、演示和测试说明。
- **检查实现：**从核心代码、逐样本证据与 CI 记录核对结论。

每个项目保持独立仓库；本页只做分类导航。
