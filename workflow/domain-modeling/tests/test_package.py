"""Standalone package checks, not execution of the agent workflow."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_entry_is_discoverable(self):
        entry = (ROOT / 'SKILL.md').read_text()
        self.assertTrue(entry.startswith('---\n'))
        frontmatter = entry.split('---', 2)[1]
        self.assertIn('name: domain-modeling\n', frontmatter)
        self.assertRegex(frontmatter, r'\ndescription: \S[^\n]+')
        self.assertNotIn('disable-model-invocation: true', frontmatter)

    def test_markdown_links_stay_inside_the_package(self):
        for path in ROOT.rglob('*.md'):
            with self.subTest(path=path.relative_to(ROOT)):
                text = path.read_text()
                self.assertNotIn('/Users/', text)
                self.assertNotIn('BEGIN PRIVATE KEY', text)
                prose = re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '', text,
                               flags=re.M | re.S)
                for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', prose):
                    if re.match(r'https?://|#|mailto:', target):
                        continue
                    resolved = path.parent / target.split('#')[0]
                    self.assertTrue(resolved.exists(), f'{path}: missing {target}')
                    self.assertTrue(resolved.resolve().is_relative_to(ROOT.resolve()),
                                    f'{path}: external file dependency {target}')


if __name__ == '__main__':
    unittest.main()
