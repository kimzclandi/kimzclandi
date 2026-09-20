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
            self.assertEqual(collect_targets(root),{'https://raw.githubusercontent.com/kimzclandi/SmallModelQAFinetuningAndQuantization/main/README.md'})
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
                {'https://raw.githubusercontent.com/kimzclandi/kimzclandi/main/README.md'},
            )
