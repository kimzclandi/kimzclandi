# kimzclandi｜数据工程与模型实验

**简体中文** | [English](README.en.md)

![Project wordmark](.github/project-header.svg)

[![CI](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml/badge.svg)](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml)
[![Stars](https://img.shields.io/github/stars/kimzclandi/kimzclandi?style=flat)](https://github.com/kimzclandi/kimzclandi/stargazers) [License status](#license)

围绕数据加工与质量、工程可靠性、视觉模型评测及评测驱动的数据迭代开展实验。以下仓库提供可运行代码、逐条结果与复现说明；代码、测试和文档使用 AI 辅助开发，具体贡献与上游归属见各项目。

[项目状态与最小运行方式](docs/PROJECT_STATUS.md) · [全部公开仓库](https://github.com/kimzclandi?tab=repositories)

## 主要项目

### 1. 中文文本数据处理与检索评测 · 可追溯的中文数据加工

将公开中文文段转为可检查的数据资产：质量算子、Ray 任务、内容寻址缓存、原子快照与 SQLite 血缘，并用检索失败分析比较切块方法。保存了串行/Ray 一致性、故障恢复和逐题检索结果；重叠切块改善证据覆盖，同时增加索引与查询成本。当前为单机小语料实验，没有 Ray 加速证据。

[项目](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval) · [运行](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval/blob/main/docs/REPRODUCE.md) · [结果](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval/blob/main/reports/RESULTS.md)

### 2. 面向目标检测的数据选择与训练对照 · 固定预算下的检测数据选择

在 BDD100K 小样本上比较随机与定向选样，仅微调预训练检测器的 ROI 预测头。提供三种子、匹配训练步数的对照、失败切片及排序机制诊断；当前未证明定向选择稳定优于随机。Ray 扩展仅在单机验证。

[项目与运行](https://github.com/kimzclandi/ObjectDetectionDataSelection) · [训练对照](https://github.com/kimzclandi/ObjectDetectionDataSelection/blob/main/docs/FAILURE_V2_REPORT.md) · [机制诊断](https://github.com/kimzclandi/ObjectDetectionDataSelection/blob/main/docs/DIAGNOSIS_V3_REPORT.md)

### 3. 视觉语言模型的图像依赖性评测 · 视觉输入干预与失败分析

固定 SmolVLM，对合成场景执行原图、空白图和错配图干预，保存 90 题 × 三种输入、共 270 次真实生成与配对切片结果。观察到的视觉贡献主要来自空间题；这是推理评测，没有模型训练收益。历史 metadata 规则演示与真实推理分开记录。

[项目](https://github.com/kimzclandi/VLMImageDependenceEvaluation) · [运行](https://github.com/kimzclandi/VLMImageDependenceEvaluation/blob/main/docs/RUNNING.md) · [干预结果](https://github.com/kimzclandi/VLMImageDependenceEvaluation/blob/main/docs/GROUNDING_V3_REPORT.md)

### 4. 小语言模型问答微调与量化实验 · 数据覆盖、训练与量化对照

围绕小模型抽取式问答，记录 LoRA、响应蒸馏、数据覆盖与同框架量化。新增参考标签质量对照完成9次训练：同题修正目标在96题留出集上将平均严格EM从17.36%提高到24.31%，差值区间为[+1.04,+13.54]个百分点；使用了参考标签，不是无标注筛选收益。新增DRCD外部96题评测中，两组平均EM均为57.29%，差值区间[-5.21,+4.86]个百分点，未复现上述正向主比较。自动核验器失败、历史训练候选未通过采用门槛，以及Q8的限定质量保持结果均保留；未作业务部署验证。

[项目](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization) · [运行](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization/blob/main/docs/QUALITY_STUDY_RELEASE.md) · [质量对照与限制](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization/blob/main/reports/quality-study-20260920/RESULTS.md) · [外部评测](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization/blob/main/docs/EXTERNAL_DRCD.md)

## 工程可靠性

| 项目 | 独立问题与验证边界 |
|---|---|
| [基于租约的分片任务调度与故障恢复](https://github.com/kimzclandi/LeaseBasedShardScheduling) | SQLite 租约、fencing token、幂等提交与主动故障实验；单机多进程，不代表多机生产系统或任务只执行一次。 |

完整指标、负结果、数据许可与适用范围保留在各仓库。CI 的离线证据检查、实际推理与模型训练按项目分别说明。

[全部公开仓库](https://github.com/kimzclandi?tab=repositories)

## 维护与本地检查

本仓库维护个人主页和项目导航，无需安装模型或业务服务。Python 3.10+：

```sh
git clone https://github.com/kimzclandi/kimzclandi.git
cd kimzclandi
python3 -m unittest discover -s tests -v
python3 scripts/verify_navigation.py
```

导航检查需要网络，会读取关联仓库的公开页面。

## Contributing / 参与贡献

[贡献指南](CONTRIBUTING.md) · [行为准则](CODE_OF_CONDUCT.md) · [结构与维护](docs/MAINTAINING.md)

[反馈问题](https://github.com/kimzclandi/kimzclandi/issues/new?template=bug_report.yml) · [建议功能](https://github.com/kimzclandi/kimzclandi/issues/new?template=feature_request.yml)

## License

本主页仓库尚未指定许可证。各链接项目的代码、数据和模型许可请以对应仓库为准。

[项目名称与兼容性说明 / Naming and compatibility](docs/NAMING.md)
