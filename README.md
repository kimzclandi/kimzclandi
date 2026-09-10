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
| 实际产物 | 保留 240 条规则样本与 108 条历史增强；新增 72 道真实 VLM 评测题、144 次生成及 6 条开发集增强 |
| 展示能力 | 图像输入隔离、场景族切分、配对实验、失败分母、开发集挖掘与数据血缘 |
| 技术栈 | Python · PyTorch · Transformers · Pillow · Streamlit · pytest · GitHub Actions |
| 验证边界 | 真实 SmolVLM CPU 推理 + 独立规则历史；无模型训练、真机实验或训练收益 |

**从这里开始：** [中文介绍与启动](https://github.com/kimzclandi/vlm-data-flywheel-lab/blob/main/README.zh-CN.md) · [实际实验报告](https://github.com/kimzclandi/vlm-data-flywheel-lab/blob/main/docs/REAL_VLM_EXPERIMENT.md) · [数据策略](https://github.com/kimzclandi/vlm-data-flywheel-lab/blob/main/docs/DATA_STRATEGY.md) · [核心代码](https://github.com/kimzclandi/vlm-data-flywheel-lab/tree/main/src/flywheel) · [CI 状态](https://github.com/kimzclandi/vlm-data-flywheel-lab/actions)

> 真实 VLM 保留集基础/观察提示均为 61.1%，未支持改进假设；开发集多数答案先验也达到 61.1%，因此不声称视觉 grounding 收益。历史规则候选总体提高但计数退化，被 REJECT；这些都不是训练收益。

<a id="autonomous-driving"></a>
## 02 · 自动驾驶

### [Driving Data Engine · 道路长尾数据闭环](https://github.com/kimzclandi/driving-data-engine)

在固定数据预算下比较采样策略，用真实检测头训练和可恢复的数据流程检验结果。

`真实道路图像 → 质量检查 → 模型推理 → 样本筛选 → 实际微调 → 切片评测与回归`

| 查看维度 | 项目内容 |
|---|---|
| 关注问题 | 哪些道路图像值得进入训练，怎样区分数据收益与额外训练的影响 |
| 实际产物 | 240 张 BDD100K 图像实验；三策略 × 三随机种子；三组匹配训练步数消融 |
| 真实 VLM | SmolVLM 昼夜标签实验，比较自由生成与有限标签解码，保留格式错误和语义分歧 |
| 数据工程 | 来源与版本追踪、Parquet/DuckDB、SQLite 幂等恢复、单机 Ray Data 一致性与吞吐实验 |
| 技术栈 | Python · PyTorch · Transformers · Ray Data · DuckDB · Streamlit · pytest · GitHub Actions |
| 验证边界 | 仅微调检测器 ROI 预测头；公开数据小规模实验；未证明显著策略收益、人工降本或 PB 级处理能力 |

**从这里开始：** [启动与结果](https://github.com/kimzclandi/driving-data-engine#readme) · [实际实验报告](https://github.com/kimzclandi/driving-data-engine/blob/main/docs/EXPERIMENT_REPORT.md) · [VLM 质检](https://github.com/kimzclandi/driving-data-engine/blob/main/docs/VLM_QUALITY.md) · [岗位能力与证据](https://github.com/kimzclandi/driving-data-engine/blob/main/docs/JD_EVIDENCE.md) · [CI 状态](https://github.com/kimzclandi/driving-data-engine/actions)

> 项目保留了不支持预期的结果：不确定性采样未稳定优于随机组，小规模 Ray 扫描慢于串行；VLM 输出格式合法也不保证语义正确。每项结论均有配置和原始报告可核查。

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
