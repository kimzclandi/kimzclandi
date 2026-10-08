# kimzclandi | Model inference, compression and data engineering

[简体中文](README.md) | **English**

![Model inference, compression and data engineering](.github/project-header.svg)

[![Navigation](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml/badge.svg)](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml)

Experiments in small-model distillation and quantization, Cache / Attention, performance analysis and reproducible data pipelines. Projects retain implementations, fixed configurations, raw records and failure analysis, distinguishing engineering checks from model-quality and performance conclusions.

[Project status and verification](docs/PROJECT_STATUS.md) · [Naming and compatibility](docs/NAMING.md) · [Public repositories](https://github.com/kimzclandi?tab=repositories)

## Core projects

### 01 · Model inference optimization and performance analysis

[inference-compression-lab](https://github.com/kimzclandi/inference-compression-lab) · Python / ONNX Runtime / MLX / Metal

CPU hot-path pruning, Cache experiments and Attention numerical checks, including native-framework controls. Under a fixed M4 Max CPU workload, hot-request computation including ranking and abstention decreased from **68.681 to 55.342 ms**; `load_service` initialization decreased from **17.919 to 5.139 s**, excluding process startup and request inference.

Negative results remain visible: Metal residual-add + RMSNorm was approximately **23.8% slower** than the compiled native path; real-Qwen native Cache reservation failed its speed gate. Mac records do not establish CUDA / Ascend measurements or production-service gains.

[Hot path and records](https://github.com/kimzclandi/inference-compression-lab/blob/codex/research-prerelease/docs/qa-risk-pruning.md) · [Initialization](https://github.com/kimzclandi/inference-compression-lab/blob/codex/research-prerelease/docs/qa-risk-startup.md) · [Attention](https://github.com/kimzclandi/inference-compression-lab/blob/codex/research-prerelease/docs/attention-backend-study.md) · [Native Cache control](https://github.com/kimzclandi/inference-compression-lab/blob/codex/research-prerelease/docs/qwen-cache-reservation.md) · [Metal negative result](https://github.com/kimzclandi/inference-compression-lab/blob/codex/research-prerelease/docs/metal-residual-rmsnorm.md)

### 02 · Small-model distillation and quantization evaluation

[SmallModelQAFinetuningAndQuantization](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization) · PyTorch / LoRA / Full-vocabulary KL / MLX

Fixed Qwen teacher/student identities, full-vocabulary logits caches for answer tokens, CE + temperature-scaled KL training and matched gold-SFT controls. v2 used **242 TRAIN examples, 3 seeds × 242 steps**. Normalized EM on 74 dev questions was **60.36% ± 2.81%**, below gold-SFT at **64.86% ± 1.35%**; this does not show a quality advantage from soft targets (mean ± sample standard deviation over 3 seeds).

Quantization records separately report weight size, inference timing and per-question quality, retaining Q4 quality failures, historical response distillation and external evaluation. The reused dev set is not independent quality confirmation. Base model and quantization capabilities come from upstream frameworks.

[Training and data protocol](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization/blob/main/docs/LOGITS_DISTILLATION_V2.md) · [Per-question results and controls](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization/blob/main/reports/logits-distillation-v2/RESULTS.md) · [Code and evidence map](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization/blob/main/docs/EVIDENCE_MAP.md) · [Contributions](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization/blob/main/CONTRIBUTIONS.md)

## Supporting project

### 03 · Chinese text processing and retrieval

[ChineseTextProcessingAndRetrieval](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval) · Ray / SQLite / BM25

Quality checks, immutable snapshots, lineage and recovery over **2,403 passages and 10,142 candidate questions**. Overlapping chunks raised held-out span-hit@3 from **81.25% to 89.38%**, while document recall@3 fell from **95.625% to 95.00%**, chunk count grew **40.14%**, and median query time rose from **7.50 to 12.04 ms**. Ray was slower than serial at this scale.

A later fixed, same-run PreparedBM25 comparison measured approximately **1.86–1.87×**, preserving exact results for 640 query-index pairs and 1,920 scores with O(V+N) additional index state. Query optimization and the earlier chunking-quality experiment remain separate studies.

[Run](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval/blob/main/docs/REPRODUCE.md) · [Retrieval results and costs](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval/blob/main/reports/RESULTS.md) · [Query optimization](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval/blob/main/docs/BM25_EXACT_OPTIMIZATION.md) · [Recovery and parity](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval/blob/main/docs/EVIDENCE_MAP.md)

## Other work

| Project | Question and scope |
|---|---|
| [Lease-based shard scheduling and recovery](https://github.com/kimzclandi/LeaseBasedShardScheduling) | SQLite leases, fencing and idempotent commits; single-machine processes, no demonstrated multi-worker speedup. |
| [AgentGate](https://github.com/kimzclandi/AgentGate) | Go tool authorization, parameter-bound approvals and audit; co-authored, single-instance prototype. |
| [Object-detection data selection and training controls](https://github.com/kimzclandi/ObjectDetectionDataSelection) | Small-sample BDD100K, ROI-head training; targeted selection did not consistently beat random. |
| [VLM image-dependence evaluation](https://github.com/kimzclandi/VLMImageDependenceEvaluation) | Fixed SmolVLM, 90 questions × three visual interventions; inference evaluation without training gains. |
| [Panda obstacle-aware posture control](https://github.com/kimzclandi/panda-obstacle-aware-posture-control) | Potential-field and PPO controls with a shared tracker; 500-episode simulation evaluation. |
| [Bearing fault diagnosis](https://github.com/kimzclandi/bearing-fault-diagnosis) | Vibration features, robustness evaluation and health-trend analysis. |

## Contributions and reproduction

Code, tests and documentation are developed with AI assistance. Individual repositories distinguish personal implementations, co-authorship and upstream framework attribution. AI-assisted implementation, framework kernels and original algorithmic contributions are separate claims.

This profile indexes default-branch material from public projects. Development branches and unmerged PRs are not presented as published results. Original failures and historical conclusions remain in their project repositories. A green CI badge covers only its workflow checks, not model quality, GPU performance or production deployment.

This repository maintains navigation only. Python 3.10+, no models required:

```sh
git clone https://github.com/kimzclandi/kimzclandi.git
cd kimzclandi
python3 -m unittest discover -s tests -v
python3 .github/scripts/check_docs.py
python3 scripts/verify_navigation.py
```

The final command needs network access and reads public default-branch READMEs and linked documents anonymously; it does not run model experiments.

[Contributing](CONTRIBUTING.md) · [Code of conduct](CODE_OF_CONDUCT.md) · [Maintenance](docs/MAINTAINING.md)

## License

This profile repository has no specified license. Consult each linked repository for code, data and model terms.
