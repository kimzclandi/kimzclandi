# 项目状态与运行方式

这份索引按已验证的工作范围组织项目。实验负结果保留在结果报告中；CI绿色表示对应检查通过，不表示业务部署或模型收益。

| 项目 | 定位与已完成部分 | 当前边界 | 最小核验入口 |
|---|---|---|---|
| [Chinese Evidence Data Engine](https://github.com/kimzclandi/chinese-evidence-data-engine) | 数据工程主项目；不可变资产、血缘、恢复和证据检索 | 单机；覆盖改善伴随索引/查询成本，无Ray加速证据 | README中的portable重建与排名核验 |
| [Domain QA Lab](https://github.com/kimzclandi/domain-qa-lab) | 模型实验主项目；训练、数据质量对照、量化与冻结评估 | 新质量实验使用参考标签；自动核验器失败；无业务部署 | `scripts/verify_quality_release.py`；真实推理另有两题CPU入口 |
| [AI Data Shard Lab](https://github.com/kimzclandi/ai-data-shard-lab) | 可靠性主项目；租约、fencing、幂等提交及主动故障 | 单机多进程；不是任务只执行一次 | 标准库测试、`scripts/verify_evidence.py` |
| [Driving Data Engine](https://github.com/kimzclandi/driving-data-engine) | 视觉训练实验；固定预算、多seed与失败切片 | 小样本、仅ROI预测头；定向未稳定优于随机 | `scripts/verify_artifacts.py`；模型重跑另需数据 |
| [VLM Data Flywheel Lab](https://github.com/kimzclandi/vlm-data-flywheel-lab) | 视觉推理实验；合成图像三种干预与逐条预测 | 固定模型、无训练；未验证真实相机/机器人 | `scripts/verify_grounding.py` |
| [AgentGate](https://github.com/kimzclandi/AgentGate) | 工程参考实现；Go授权、参数绑定审批、事务和撤销 | 单实例、合成业务资源；代码许可证待共同作者决定 | `make check`、`make demo`；真实本地模型另需Ollama |
| [Road Video Miner](https://github.com/kimzclandi/road-video-miner) | 配套研究；图像序列选段与覆盖回放 | 简单直方图特征；无下游训练，未证明稳定优于随机 | NumPy轻量环境运行`portable_replay.py` |
| [Detection Label Audit](https://github.com/kimzclandi/detection-label-audit) | 配套研究；合成污染排序和定位归因 | 真实标签效用未验证，59图保留池尚未评分 | Python标准库运行`replay.py` |
| [Profile](https://github.com/kimzclandi/kimzclandi) | 跨项目导航、贡献与验证边界索引 | 不承载独立模型实验 | `python scripts/verify_navigation.py` |

各入口均须按对应仓库README准备环境。离线重算、重新执行数据流水线、真实模型推理和重新训练分别标注；不把查看已保存结果算作重新运行实验。

## 2026-09-20维护

- 同步Domain QA新公开的参考标签质量对照和一次留出评估；保留历史候选未通过门槛及自动核验器失败。
- Road Video Miner增加只依赖NumPy的回放环境；Detection Label Audit增加标准库回放入口，界面与完整实验环境仍单独保留。
- 主项目与配套研究分开呈现，不为制造活跃记录而追加无关功能。所有原始预测、冻结协议、无效对照和负结果保持不变。
- 许可证决策、独立人工裁决、真实外部数据及生产部署需要相应事实与证据；本次维护不代替这些验证。
