"""Offline structure checks; these do not execute the agent's prose workflow."""
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def check_package(self, root, name, command_only):
        entry = (root / 'SKILL.md').read_text()
        self.assertTrue(entry.startswith('---\n'))
        frontmatter = entry.split('---', 2)[1]
        self.assertIn(f'name: {name}\n', frontmatter)
        self.assertRegex(frontmatter, r'\ndescription: \S[^\n]+')
        self.assertEqual('disable-model-invocation: true' in frontmatter, command_only)
        for path in root.rglob('*.md'):
            text = path.read_text()
            self.assertNotIn('/Users/', text, str(path))
            self.assertNotIn('BEGIN PRIVATE KEY', text, str(path))
            # Fenced snippets are example output for a target project, not package links.
            prose = re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '', text, flags=re.M | re.S)
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', prose):
                if re.match(r'https?://|#|mailto:', target):
                    continue
                resolved = path.parent / target.split('#')[0]
                self.assertTrue(resolved.exists(), f'{path}: missing {target}')
                self.assertTrue(resolved.resolve().is_relative_to(root.resolve()),
                                f'{path}: undeclared sibling file dependency {target}')

    def test_setup_package_is_self_contained_for_local_work(self):
        self.check_package(ROOT, 'setup-project', command_only=True)

    def test_github_companion_packaging_when_present(self):
        companion = ROOT.parent / 'github-repo-setup'
        if not companion.exists():
            self.skipTest('Standalone setup copy; companion packaging not checked')
        self.check_package(companion, 'github-repo-setup', command_only=False)


if __name__ == '__main__':
    unittest.main()
