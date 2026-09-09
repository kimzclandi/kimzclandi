# kimzclandi · 项目导航

**AI 数据与评测 · 自动驾驶 · 机器人与具身智能**

AI Data & Evaluation · Autonomous Driving · Robotics & Embodied AI

这里按方向整理我的公开项目，方便查看代码、运行方法和实验依据。

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
| 实际产物 | 240 条原创评测样本、108 条增强数据、逐样本结果与可交互 Dashboard |
| 展示能力 | 数据策略、指标设计、失败分析、实验复现与产品决策 |
| 技术栈 | Python · Pillow · Streamlit · pytest · GitHub Actions |
| 验证边界 | 离线确定性参考规则；未进行真实 VLM 训练或真机实验 |

**从这里开始：** [中文介绍与启动](https://github.com/kimzclandi/vlm-data-flywheel-lab/blob/main/README.zh-CN.md) · [实际实验报告](https://github.com/kimzclandi/vlm-data-flywheel-lab/blob/main/docs/EXPERIMENT_REPORT.md) · [数据策略](https://github.com/kimzclandi/vlm-data-flywheel-lab/blob/main/docs/DATA_STRATEGY.md) · [核心代码](https://github.com/kimzclandi/vlm-data-flywheel-lab/tree/main/src/flywheel) · [CI 状态](https://github.com/kimzclandi/vlm-data-flywheel-lab/actions)

> 这个项目演示了一个关键判断：候选版本的总体准确率提高，仍可能因计数能力退化而被拒绝。当前结果证明的是评测与决策流程，不是模型学习收益。

<a id="autonomous-driving"></a>
## 02 · 自动驾驶

**目前暂无该分类的公开项目。**

后续项目可围绕感知与融合、定位、规划控制、场景评测组织；这些是分类范围，不代表已经完成的工作。

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
