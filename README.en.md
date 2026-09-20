# kimzclandi · Data Engineering and Model Experiments

[简体中文](README.md) | **English**

![Project wordmark](.github/project-header.svg)

[![CI](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml/badge.svg)](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml)
[![Stars](https://img.shields.io/github/stars/kimzclandi/kimzclandi?style=flat)](https://github.com/kimzclandi/kimzclandi/stargazers) [License status](#license)

Experiments in data processing and quality, engineering reliability, visual-model evaluation and evaluation-driven data iteration. These repositories provide runnable code, per-example results and reproduction instructions. Code, tests and documentation use AI-assisted development; each project documents contributions and upstream attribution.

[Project status and minimal runs](docs/PROJECT_STATUS.md) · [All public repositories](https://github.com/kimzclandi?tab=repositories)

## Main projects

### 1. Chinese text processing and retrieval evaluation

Turn public Chinese passages into inspectable data assets using quality operators, Ray tasks, content-addressed caching, atomic snapshots and SQLite lineage. Retrieval failures guide chunking comparisons. Saved evidence covers serial/Ray equivalence, recovery and per-question retrieval. Overlap improves evidence coverage while increasing index size and query cost. This is a small single-machine corpus experiment, with no demonstrated Ray speedup.

[Project](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval) · [Run](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval/blob/main/docs/REPRODUCE.md) · [Results](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval/blob/main/reports/RESULTS.md)

### 2. Data selection and controlled training for object detection

Compare random and targeted selection on a small BDD100K sample, finetuning only a pretrained detector's ROI predictor head. Includes three-seed, matched-step controls, failure slices and ranking-mechanism diagnostics. A stable advantage of targeted selection over random has not been demonstrated. Ray extensions are verified only on one machine.

[Project and running](https://github.com/kimzclandi/ObjectDetectionDataSelection) · [Training comparison](https://github.com/kimzclandi/ObjectDetectionDataSelection/blob/main/docs/FAILURE_V2_REPORT.md) · [Mechanism diagnostics](https://github.com/kimzclandi/ObjectDetectionDataSelection/blob/main/docs/DIAGNOSIS_V3_REPORT.md)

### 3. Visual-input dependence in a vision-language model

With fixed SmolVLM, compare original, blank and mismatched images on synthetic scenes. Records contain 90 questions × three conditions, or 270 actual generations, with paired slices. Observed visual contribution mainly comes from spatial questions. This is inference evaluation, not a training gain. Historical metadata-rule demonstrations are recorded separately from actual inference.

[Project](https://github.com/kimzclandi/VLMImageDependenceEvaluation) · [Run](https://github.com/kimzclandi/VLMImageDependenceEvaluation/blob/main/docs/RUNNING.md) · [Intervention results](https://github.com/kimzclandi/VLMImageDependenceEvaluation/blob/main/docs/GROUNDING_V3_REPORT.md)

### 4. Small-model QA finetuning and quantization

Extractive-QA studies covering LoRA, response distillation, data coverage and same-framework quantization. Nine new reference-label quality-control runs raised mean strict EM on a 96-question holdout from 17.36% to 24.31% by correcting targets for the same questions; the difference interval is [+1.04,+13.54] points. Reference labels were used, so this is not an unlabeled-filtering gain. On a new 96-question DRCD external evaluation, both groups achieved mean EM of 57.29%, with difference interval [-5.21,+4.86] points; the positive primary comparison did not replicate. Automatic-verifier failures, historical candidates failing adoption gates and bounded Q8 quality-preservation results remain documented. No business deployment validation.

[Project](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization) · [Run](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization/blob/main/docs/QUALITY_STUDY_RELEASE.md) · [Quality comparison and limits](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization/blob/main/reports/quality-study-20260920/RESULTS.md) · [External evaluation](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization/blob/main/docs/EXTERNAL_DRCD.md)

## Engineering reliability

| Project | Problem and verified scope |
|---|---|
| [Lease-based shard scheduling and recovery](https://github.com/kimzclandi/LeaseBasedShardScheduling) | SQLite leases, fencing tokens, idempotent commits and injected failures; single-machine multi-process behavior, not multi-machine production operation or exactly-once execution. |

Full metrics, negative results, data licensing and scope remain in each repository. Offline CI evidence checks, actual inference and model training are distinguished per project. Linked technical documents retain their original language.

[All public repositories](https://github.com/kimzclandi?tab=repositories)

## Maintenance and local checks

This repository maintains a profile and project navigation. No model or business-service installation is needed. Python 3.10+:

```sh
git clone https://github.com/kimzclandi/kimzclandi.git
cd kimzclandi
python3 -m unittest discover -s tests -v
python3 scripts/verify_navigation.py
```

Navigation verification requires network access and reads the linked repositories' public pages.

## Contributing

[Guide](CONTRIBUTING.md) · [Code of conduct](CODE_OF_CONDUCT.md) · [Structure/maintenance](docs/MAINTAINING.md)

[Report an issue](https://github.com/kimzclandi/kimzclandi/issues/new?template=bug_report.yml) · [Suggest a feature](https://github.com/kimzclandi/kimzclandi/issues/new?template=feature_request.yml)

## License

This profile repository has no designated license. Consult each linked project for its code, data and model licenses.

[Naming and compatibility](docs/NAMING.md)
