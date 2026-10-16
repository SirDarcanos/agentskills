"""Offline structure checks; these do not execute the agent's prose workflow."""
import re
import shutil
import tempfile
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

    def test_concurrency_is_a_lead_decision_not_a_setup_default_cap(self):
        discovery = (ROOT / 'references/discovery.md').read_text()
        for clause in ('Leave routine worker concurrency to the delivery lead',
                       'do not invent a numerical worker ceiling',
                       'preserve existing consumer-project concurrency limits',
                       'exact reconciliation is approved', 'finite assignment runtime and repair bounds'):
            self.assertIn(clause, discovery)
        self.assertNotIn('Use finite runtime/capacity and repair bounds', discovery)

    def test_setup_package_has_only_package_local_file_links(self):
        self.check_package(ROOT, 'setup-project', command_only=True)

    def test_setup_copied_without_sibling_companions(self):
        with tempfile.TemporaryDirectory() as directory:
            copied = Path(directory) / 'isolated-setup'
            shutil.copytree(ROOT, copied)
            self.check_package(copied, 'setup-project', command_only=True)

    def test_domain_companion_packaging_when_present(self):
        companion = ROOT.parent / 'domain-modeling'
        if not companion.exists():
            self.skipTest('Standalone setup copy; domain companion packaging not checked')
        self.check_package(companion, 'domain-modeling', command_only=False)

    def test_github_companion_packaging_when_present(self):
        companion = ROOT.parent / 'github-repo-setup'
        if not companion.exists():
            self.skipTest('Standalone setup copy; companion packaging not checked')
        self.check_package(companion, 'github-repo-setup', command_only=False)


if __name__ == '__main__':
    unittest.main()
