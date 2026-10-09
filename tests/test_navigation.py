import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from verify_navigation import collect_targets


class NavigationTests(unittest.TestCase):
    def test_nested_docs_are_checked(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'docs').mkdir()
            (root/'README.md').write_text('[status](docs/status.md)')
            (root/'docs/status.md').write_text('[repo](https://github.com/kimzclandi/SmallModelQAFinetuningAndQuantization)')
            self.assertEqual(collect_targets(root),{'https://raw.githubusercontent.com/kimzclandi/SmallModelQAFinetuningAndQuantization/HEAD/README.md'})
            (root/'docs/status.md').write_text('[missing](absent.md)')
            with self.assertRaisesRegex(ValueError,'Missing local'):collect_targets(root)

    def test_empty_catalog_cannot_pass(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'README.md').write_text('empty')
            with self.assertRaisesRegex(ValueError,'No public'):collect_targets(root)

    def test_clone_url_resolves_to_repository_readme(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'README.md').write_text(
                'git clone https://github.com/kimzclandi/kimzclandi.git\n'
            )
            self.assertEqual(
                collect_targets(root),
                {'https://raw.githubusercontent.com/kimzclandi/kimzclandi/HEAD/README.md'},
            )

    def test_non_main_default_and_slash_branch_document(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'README.md').write_text(
                '[repo](https://github.com/kimzclandi/inference-compression-lab)\n'
                '[doc](https://github.com/kimzclandi/inference-compression-lab/'
                'blob/codex/research-prerelease/docs/attention-backend-study.md#scope)'
            )
            self.assertEqual(collect_targets(root), {
                'https://raw.githubusercontent.com/kimzclandi/inference-compression-lab/HEAD/README.md',
                'https://raw.githubusercontent.com/kimzclandi/inference-compression-lab/'
                'codex/research-prerelease/docs/attention-backend-study.md',
            })

    def test_english_only_targets_and_missing_local_links_are_checked(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'README.md').write_text('[English](README.en.md)')
            english = root / 'README.en.md'
            english.write_text('[repo](https://github.com/kimzclandi/AgentGate)')
            self.assertEqual(collect_targets(root), {
                'https://raw.githubusercontent.com/kimzclandi/AgentGate/HEAD/README.md',
            })
            english.write_text('[missing](missing.md)')
            with self.assertRaisesRegex(ValueError, 'Missing local'):
                collect_targets(root)
