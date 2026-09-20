# 项目状态与运行方式

这份索引按已验证的工作范围组织项目。实验负结果保留在结果报告中；CI绿色表示对应检查通过，不表示业务部署或模型收益。

| 项目 | 定位与已完成部分 | 当前边界 | 最小核验入口 |
|---|---|---|---|
| [中文文本数据处理与检索评测](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval) | 数据工程主项目；不可变资产、血缘、恢复和证据检索 | 单机；覆盖改善伴随索引/查询成本，无Ray加速证据 | README中的portable重建与排名核验 |
| [小语言模型问答微调与量化实验](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization) | 模型实验主项目；训练、数据质量对照、量化与冻结评估 | 使用参考标签；CMRC正向主比较未在DRCD外部96题复现；无业务部署 | `scripts/verify_quality_release.py`与`scripts/verify_external_drcd.py`；完整训练入口已同机重跑 |
| [基于租约的分片任务调度与故障恢复](https://github.com/kimzclandi/LeaseBasedShardScheduling) | 可靠性工程补充；租约、fencing、幂等提交及主动故障 | 单机多进程；不是任务只执行一次 | 标准库测试、`scripts/verify_evidence.py` |
| [面向目标检测的数据选择与训练对照](https://github.com/kimzclandi/ObjectDetectionDataSelection) | 视觉训练实验；固定预算、多seed与失败切片 | 小样本、仅ROI预测头；定向未稳定优于随机 | `scripts/verify_artifacts.py`；模型重跑另需数据 |
| [视觉语言模型的图像依赖性评测](https://github.com/kimzclandi/VLMImageDependenceEvaluation) | 视觉推理实验；合成图像三种干预与逐条预测 | 固定模型、无训练；未验证真实相机/机器人 | `scripts/verify_grounding.py` |
| [Profile](https://github.com/kimzclandi/kimzclandi) | 跨项目导航、贡献与验证边界索引 | 不承载独立模型实验 | `python scripts/verify_navigation.py` |

各入口均须按对应仓库README准备环境。离线重算、重新执行数据流水线、真实模型推理和重新训练分别标注；不把查看已保存结果算作重新运行实验。
