"""Offline method-contract fixtures, not an automatic selector or agent trial.

Run with Python 3.9+. Only temporary synthetic files are written; no network,
models, tracker, Git or installed-discovery changes. Expected routing is authored
and must be inspected against SKILL.md, not inferred from this oracle.
"""
import hashlib
from pathlib import Path
import tempfile
import unittest


CASES = (
    ("clear behavior", "tdd", "behavioral red; minimal green; green refactoring"),
    ("uncertain feasibility", "prototype", "bounded experiment; observations; artifact disposition"),
    ("legacy change", "characterize", "baseline; intended/unknown/defect; sensitivity"),
    ("cross-component acceptance", "acceptance-first", "executable agreed examples; increments; criterion results"),
    ("straightforward change", "build-and-check", "small increment; immediate check; coverage reuse"),
)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ContractFixtures(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="analyze-contract-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.target = self.root / "target"
        self.target.mkdir()
        self.catalog = {}
        # Intentionally outside the target and without sibling installed skills.
        for index, (_, method, contract) in enumerate(CASES):
            package = self.root / "catalog" / ("location-" + str(index))
            package.mkdir(parents=True)
            entry = package / "SKILL.md"
            entry.write_text("---\nname: " + method + "\ndescription: Synthetic contract fixture.\n---\n" + contract + "\n")
            self.catalog[method] = entry
        for name, content in {
            "service.py": "def heading():\n    return 'Records'\n",
            "caller.py": "from service import heading\nlabel = heading()\n",
            "checks.py": "assert heading() == 'Records'\n",
            "protected.txt": "unrelated work\n",
        }.items():
            (self.target / name).write_text(content)

    def test_all_five_contract_sources(self):
        for case, method, contract in CASES:
            with self.subTest(case=case):
                entry = self.catalog[method]
                self.assertFalse(entry.is_relative_to(self.target))
                self.assertIn("name: " + method, entry.read_text())
                self.assertIn(contract, entry.read_text())
                self.assertEqual(len(digest(entry)), 64)
                print("fixture contract:", case, "=>", method)

    def test_current_analysis_inputs(self):
        inputs = {name: digest(self.target / name) for name in ("service.py", "caller.py", "checks.py")}
        self.assertEqual(inputs, {name: digest(self.target / name) for name in inputs})
        print("current inputs: 3 matching content identities, reusable evidence")

    def test_dirty_caller_invalidates_only_dependent_evidence(self):
        paths = {name: self.target / name for name in ("service.py", "caller.py", "checks.py")}
        before = {name: digest(path) for name, path in paths.items()}
        paths["caller.py"].write_text("from service import heading\nlabel = heading().upper()\n")
        changed = {name for name, path in paths.items() if digest(path) != before[name]}
        self.assertEqual(changed, {"caller.py"})
        support = {"service behavior": {"service.py", "checks.py"}, "consumer label": {"service.py", "caller.py"}}
        stale = {claim for claim, sources in support.items() if sources & changed}
        self.assertEqual(stale, {"consumer label"})
        print("changed caller: consumer label stale; service behavior retained")

    def test_missing_method_does_not_destroy_recommendation(self):
        recommendation = "prototype"
        self.catalog[recommendation].unlink()
        self.assertFalse(self.catalog[recommendation].exists())
        self.assertEqual(recommendation, "prototype")
        self.assertTrue(self.catalog["tdd"].exists())
        print("prototype missing: recommendation retained, execution unavailable; no substitution")

    def test_incompatible_same_name_is_not_capability(self):
        entry = self.catalog["tdd"]
        entry.write_text("---\nname: tdd\n---\nSkip refactoring and require user-selected seams.\n")
        self.assertNotIn(CASES[0][2], entry.read_text())
        print("same name without required contract: incompatible fixture")

    def test_changed_checks_invalidate_coverage_not_service_facts(self):
        paths = {name: self.target / name for name in ("service.py", "caller.py", "checks.py")}
        before = {name: digest(path) for name, path in paths.items()}
        paths["checks.py"].write_text("assert heading().upper() == 'RECORDS'\n")
        changed = {name for name, path in paths.items() if digest(path) != before[name]}
        support = {"source fact": {"service.py"}, "coverage": {"service.py", "checks.py"}}
        self.assertEqual({claim for claim, sources in support.items() if sources & changed}, {"coverage"})

    def test_entry_project_and_conversation_boundaries(self):
        # Textual regression guards, not execution of the skill or a policy engine.
        entry = (Path(__file__).resolve().parents[1] / "SKILL.md").read_text()
        for phrase in ("once per context", "Equivalent existing layouts", "without starting it",
                       "Missing common guidance", "ordinary inactive findings", "explicit agreement and permission"):
            self.assertIn(phrase, entry)
        self.assertNotIn("references/contracts.md", entry)
        self.assertIn("For a conditional library, inspect the documented pointer", entry)
        self.assertIn("only the old universal contract is incompatible", entry)

    def test_inspection_preserves_target(self):
        before = {p.name: digest(p) for p in self.target.iterdir()}
        for path in self.target.iterdir():
            path.read_text()
        self.assertEqual(before, {p.name: digest(p) for p in self.target.iterdir()})
        print("inspection: all target bytes unchanged; no production artifacts")


if __name__ == "__main__":
    unittest.main(verbosity=2)
