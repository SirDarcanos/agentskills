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

    def test_compact_agreement_contract_and_stage_boundaries(self):
        """Static contract guard, not an agent or semantic-agreement parser."""
        contract = (ROOT / 'references/documentation-contract.md').read_text()
        for clause in ('not filenames', 'One concise working agreement',
                       'missing', 'conflict', 'unverifiable',
                       'no autonomous assessment permission',
                       'without a second full-text approval',
                       'before PR preparation/publication',
                       'Persistence is user-directed',
                       'two-cycle automatic repair ceiling',
                       'explicit agreement/permission',
                       'not yet migrated', 'Leave existing Work On library targets'):
            self.assertIn(clause, contract)
        reconciliation = (ROOT / 'references/reconciliation.md').read_text()
        for clause in ('A skill upgrade is not approval', 'Equivalent guidance',
                       'no empty glossary', 'installed-copy changes'):
            self.assertIn(clause, reconciliation)

    def test_model_detail_is_conditional_and_bootstrap_is_explicit(self):
        entry = (ROOT / 'SKILL.md').read_text()
        self.assertIn('For unresolved assessment choices or a proposed policy change', entry)
        self.assertIn('Setup is a bootstrap entry', entry)
        self.assertIn('Ordinary consumers recommend reconciliation', entry)
        self.assertIn('When tracker work is approved', entry)

    def test_local_agreement_example_is_concise_and_self_contained(self):
        """Authored output example; passing does not prove setup generates it."""
        fixture = ROOT / 'tests/fixtures/local-agreement'
        entry = (fixture / 'AGENTS.md').read_text()
        agreement = (fixture / 'CONTRIBUTING.md').read_text()
        self.assertIn('(CONTRIBUTING.md)', entry)
        for clause in ('no tracker', 'Only bounded independent read-only',
                       'assessments and service startup are prohibited',
                       'at most two automatic repair cycles',
                       'before PR preparation/publication',
                       'Same-session evidence can stay in conversation'):
            self.assertIn(clause, agreement)
        self.assertEqual({p.name for p in fixture.iterdir()},
                         {'AGENTS.md', 'CONTRIBUTING.md'})
        self.assertNotIn('references/contracts.md', agreement)
        self.assertNotIn('docs/agents/', agreement)

    def test_direct_native_library_and_legacy_forwarder(self):
        library = (ROOT / 'references/native-tracker.md').read_text()
        legacy = (ROOT / 'references/issue-tracker.md').read_text()
        entry = (ROOT / 'SKILL.md').read_text()
        for clause in ('without reading `SKILL.md` or the label audit',
                       'Missing, ambiguous or incompatible',
                       'exact approved effects', 'no setup',
                       'Spec/work-ticket roles, titles and readiness',
                       'Reconciliation algorithm', 'including pagination',
                       'cross-repository identities', 'transitive blockers',
                       'ambiguous 404', 'both relationship directions',
                       'one github.com repository', 'does not manage parentage',
                       'never deletes edges or retries failed writes'):
            self.assertIn(clause, library)
        self.assertIn('(references/native-tracker.md)', entry)
        self.assertIn('(native-tracker.md)', legacy)
        self.assertIn('## Native GitHub graph', legacy)
        self.assertIn('Source changes do not update installed copies', legacy)
        self.assertNotIn('### Reconciliation algorithm', legacy)
        self.assertNotIn('gh api --method POST', legacy)
        self.assertNotIn('## Label audit', library)
        self.assertNotIn('### Present the labels step', library)

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
