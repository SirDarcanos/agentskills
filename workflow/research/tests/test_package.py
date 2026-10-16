"""Offline package/wording guards, not research execution or agent trials."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_project_and_standalone_boundaries(self):
        entry = (ROOT / 'SKILL.md').read_text()
        self.assertTrue(entry.startswith('---\nname: research\n'))
        for phrase in ('once per context', 'Equivalent layouts', 'Missing common guidance',
                       'General non-project research', 'without manufacturing a project agreement',
                       'even if a retention home exists', 'without starting another stage'):
            self.assertIn(phrase, entry)
        self.assertNotIn('references/contracts.md', entry)
        self.assertIn('for a conditional library inspect the documented pointer', entry)

    def test_delegation_is_conditional_and_retains_safety(self):
        entry = (ROOT / 'SKILL.md').read_text()
        self.assertIn('For optional background work, read [delegation]', entry)
        delegation = (ROOT / 'references' / 'delegation.md').read_text()
        for phrase in ('only the old universal contract', 'block delegation, not equivalent direct research',
                       'finite timeout/turn/tool bound', 'confirmed stopped or isolated',
                       'existing checkpoint/repair allowance without resetting it'):
            self.assertIn(phrase, delegation)
        self.assertNotIn('references/contracts.md', delegation)

    def test_procedure_links_are_package_local(self):
        # The historical Clef note is preserved, not part of the live procedure.
        paths = [ROOT / 'SKILL.md', ROOT / 'README.md', *sorted((ROOT / 'references').glob('*.md'))]
        for path in paths:
            text = path.read_text()
            self.assertNotIn('/Users/', text)
            prose = re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '', text, flags=re.M | re.S)
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', prose):
                if re.match(r'https?://|#|mailto:', target):
                    continue
                resolved = path.parent / target.split('#')[0]
                self.assertTrue(resolved.exists(), f'{path}: missing {target}')
                self.assertTrue(resolved.resolve().is_relative_to(ROOT.resolve()))


if __name__ == '__main__':
    unittest.main()
