# kimzclandi

[简体中文](README.md) | **English**

[![Navigation](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml/badge.svg)](https://github.com/kimzclandi/kimzclandi/actions/workflows/navigation.yml)

Experiments in small-model distillation and quantization, Cache / Attention, performance analysis and reproducible data pipelines. Projects retain implementations, fixed configurations, raw records and failure analysis, distinguishing engineering checks from model-quality and performance conclusions.

[Project status and verification](docs/PROJECT_STATUS.md) · [Naming and compatibility](docs/NAMING.md) · [Public repositories](https://github.com/kimzclandi?tab=repositories)

## Public projects

Listed by area, without ranking. Results, limits and reproduction commands are maintained in each repository's default branch.

### Inference, compression and data

- [inference-compression-lab](https://github.com/kimzclandi/inference-compression-lab): model inference optimization and performance analysis. CPU hot-path, KV Cache, Attention and Metal experiments against native-framework controls; failed speed gates are retained, and CUDA / Ascend were not measured.
- [SmallModelQAFinetuningAndQuantization](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization): small-model distillation and quantization evaluation (two authors). Full-vocabulary logits distillation with Qwen teacher/student, matched gold-SFT controls and MLX quantization; distillation did not exceed gold-SFT and Q4 failed its quality gate.
- [ChineseTextProcessingAndRetrieval](https://github.com/kimzclandi/ChineseTextProcessingAndRetrieval): Chinese data processing and retrieval. Immutable snapshots, SQLite lineage, Ray recovery and BM25 retrieval controls; chunking gains come with recall and latency costs, and Ray was slower than serial at this scale.

### Systems and agents

- [AgentGate](https://github.com/kimzclandi/AgentGate): authorization and approval for agent tool calls (co-authored). Go implementation of parameter-bound approvals and audit; single-instance prototype.

### Visual-model evaluation

- [ObjectDetectionDataSelection](https://github.com/kimzclandi/ObjectDetectionDataSelection): object-detection data selection and training controls. Small-sample BDD100K, ROI-head training only; targeted selection did not consistently beat random.
- [VLMImageDependenceEvaluation](https://github.com/kimzclandi/VLMImageDependenceEvaluation): VLM image-dependence evaluation. Fixed SmolVLM with original, blank and mismatched image inputs; inference-only evaluation, no training.

## Non-public projects

These repositories are not public; only their names and scope are listed.

- **LeaseBasedShardScheduling**: lease-based shard scheduling and recovery. SQLite leases, fencing and idempotent commits; single-machine processes, no demonstrated multi-worker speedup.
- **panda-obstacle-aware-posture-control**: Panda obstacle-aware posture control. Simulated comparison of potential-field and PPO controls with a shared tracker; PPO reuses an upstream implementation and results are simulation-only.
- **bearing-fault-diagnosis**: bearing fault diagnosis (collaborative). CWRU vibration features, robustness evaluation and health-trend analysis; not remaining-useful-life prediction.

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
