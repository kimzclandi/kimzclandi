# 维护项目导航

本仓库与用户名同名，根目录 README 显示在个人主页；它只做导航，不计为技术项目。

主要项目依次为 chinese-evidence-data-engine、driving-data-engine、vlm-data-flywheel-lab、domain-qa-lab，分别对应数据资产与可靠性、检测数据选择、视觉输入评测、训练与量化对照。AgentGate 为合作工程补充；ai-data-shard-lab、road-video-miner 与 detection-label-audit 为配套研究。更新介绍时保留仓库名称、URL 与 Git 历史。

每个条目简要说明研究问题、实际实现、当前结果、运行入口与关键限制。指标旁写明数据范围和分母；历史规则、真实推理、预测缓存回放与训练分开说明。先核对对应仓库当前报告再更新主页，不能用旧摘要代替当前事实。

保留真实的 AI 辅助说明与共同作者归属。方法说明和实现索引通过技术文档组织；明确区分已验证结果、设计建议和后续计划。

发布前运行 `python scripts/verify_navigation.py`，检查匿名文档访问。推送后检查该提交的 Actions；徽标代替手写测试总数。不要加入本机路径、私人资料或密钥。

# Maintenance guide

## Structure

Stack: **GitHub profile / Python navigation checks**. Main paths: `README.md, docs/, scripts/, tests/`.

This is a profile/navigation repository, not an installable library. Keep project evidence in the linked project repositories.

- `.github/`: issue forms, PR template, project wordmark and Actions workflows.
- `CONTRIBUTING.md`: contributor setup and relevant local checks.
- `docs/`: explanations and maintenance guidance; historical reports retain their original scope.
- Temporary outputs and environments belong in ignored directories, never in published evidence.

## Automation

Existing project checks: [navigation.yml](../.github/workflows/navigation.yml). These remain the source of truth for the
actual test and replay commands. Workflow concurrency cancels superseded runs on the
same ref; job timeouts bound hung checks. No inference or training coverage is implied.

[Documentation CI](../.github/workflows/documentation.yml) runs a dependency-free Python
check for local file links in README, contribution/conduct guidance, the PR template and
this page. It also checks commit whitespace. It does not validate external URLs, heading
anchors, SVG rendering or every historical document. New linked files must be staged
with `git add` before the local check so they are included in `git ls-files`.

```sh
python3 .github/scripts/check_docs.py
```

## Releases

Automatic package publishing is not configured: this repository has no established
package publication contract. Use a reviewed, manually created GitHub Release only when
there is a meaningful version to distribute. Before creating a tag:

1. Run the relevant project checks and documentation checks on the exact commit.
2. Confirm Actions has passed for that same commit; record skipped model/hardware checks.
3. Review the diff for secrets, large generated files and changes to frozen evidence.
4. Confirm code, data and model licensing separately; preserve authorship and attribution.
5. Write release notes covering behavior changes, validation scope and remaining limits.

A future automated release should use explicit version tags, validate the tagged commit
and upload reviewed artifacts. Add package registry credentials and write permissions only
when that publication workflow is deliberately adopted.
