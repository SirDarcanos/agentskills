"""Offline evidence/report regression checks, not an agent-compliance engine."""
import ast
import json
import pathlib
import unittest

from fixture import generate

HERE = pathlib.Path(__file__).parent


def functions(source):
    return {node.name: ast.dump(node.body[0], include_attributes=False)
            for node in ast.walk(ast.parse(source))
            if isinstance(node, ast.FunctionDef)}


class FixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fresh = generate()
        cls.retained = json.loads((HERE / "evidence.json").read_text())
        cls.reports = (HERE / "reports.md").read_text()

    def test_identity_accounting(self):
        for data in self.fresh.values():
            before, after = functions(data["baseline_tests"]), functions(data["candidate_tests"])
            self.assertEqual(set(after) - set(before), {"test_new"})
            self.assertEqual(set(before) - set(after), {"test_duplicate"})
            self.assertEqual({name for name in before.keys() & after.keys()
                              if before[name] != after[name]}, {"test_update"})
            self.assertIn("rename from test_old.py", data["diff"])
            self.assertEqual(before["test_duplicate"], after["test_keep"])

    def test_actual_local_checks(self):
        for data in self.fresh.values():
            for key in ("baseline_check", "candidate_check"):
                self.assertIn("Ran 3 tests", data[key])
                self.assertTrue(data[key].endswith("OK"))
            self.assertNotIn("__pycache__", data["diff"])

    def test_ci_distinctions(self):
        measured, unmeasured, absent = (self.fresh[key] for key in ("measured", "unmeasured", "no-ci"))
        self.assertIn("checks:", measured["workflow"])
        self.assertNotIn("syntax:", measured["workflow"])
        self.assertIn("syntax:", unmeasured["workflow"])
        self.assertNotIn("samples", unmeasured)
        self.assertIsNone(absent["workflow"])
        self.assertEqual(absent["ci"], "")
        for data in (measured, unmeasured):
            self.assertIn("on: [pull_request]", data["workflow"])
            self.assertNotIn("deploy", data["workflow"])

    def test_measurements_are_synthetic_and_separate(self):
        samples = self.fresh["measured"]["samples"]
        self.assertIn("NOT observed hosted runs", samples["provenance"])
        self.assertEqual(samples["baseline_elapsed_seconds"] - samples["candidate_elapsed_seconds"], 20)
        self.assertEqual(samples["baseline_runner_seconds"] - samples["candidate_runner_seconds"], 20)
        self.assertEqual(samples["samples_per_state"], 1)
        self.assertIsNone(samples["billing"])
        self.assertIn("not observed hosted runs", self.reports)
        self.assertIn("25% of 80", self.reports)
        self.assertIn("28.6% of 70", self.reports)
        self.assertIn("unmeasured", self.reports)
        self.assertIn("inapplicable", self.reports)

    def test_retained_reports_trace_sources_and_blockers(self):
        for name, data in self.retained.items():
            self.assertIn(data["baseline"][:7], self.reports)
            self.assertIn(data["candidate"][:7], self.reports)
            self.assertEqual(data["baseline_tests"], self.fresh[name]["baseline_tests"])
            self.assertEqual(data["candidate_tests"], self.fresh[name]["candidate_tests"])
        self.assertEqual(self.reports.count("**1 added, 1 removed, 1 updated**"), 3)
        self.assertEqual(self.reports.count("**M1 unresolved**"), 3)
        self.assertEqual(self.reports.count("Publication blocked"), 3)
        self.assertNotIn("all tests passed", self.reports.lower())

    def test_migration_and_report_only_authority(self):
        for data in self.fresh.values():
            self.assertIn("source revert does not restore installed copies", data["migration"])
            self.assertIn("no publication, benchmarks or installed migration", data["authority"])
        self.assertIn("backup restoration is untested", self.reports)
        self.assertIn("external behavior remains unknown", self.reports)
        # Guard fixture's effect surface; actual PR publication is not simulated here.
        source = (HERE / "fixture.py").read_text()
        for command in ('"gh"', '"push"', '"merge"', '"curl"'):
            self.assertNotIn(command, source)


class SummaryExamplesTests(unittest.TestCase):
    """Static guardrails over authored pairs, not proof of agent behavior."""

    @classmethod
    def setUpClass(cls):
        cls.examples = json.loads((HERE / "summary_examples.json").read_text())

    def test_summary_length_and_evidence_separation(self):
        self.assertIn("synthetic", self.examples["provenance"])
        for case in self.examples["cases"]:
            with self.subTest(case=case["name"]):
                summary = case["summary"]
                self.assertTrue(100 <= len(summary.split()) <= 200)
                self.assertEqual(summary.count("[Supporting evidence]"), 1)
                for detail in ("internal_accounting", "python3", "SHA-256", "runner-seconds", "**1 added"):
                    self.assertNotIn(detail, summary)
                self.assertNotIn("all tests passed", summary.lower())
                self.assertTrue(case["evidence"]["checks"])

    def test_closing_and_related_references(self):
        import re
        for case in self.examples["cases"]:
            summary, evidence = case["summary"], case["evidence"]
            self.assertEqual([int(n) for n in re.findall(r"Closes #(\d+)", summary)], evidence["closes"])
            self.assertEqual([int(n) for n in re.findall(r"Refs #(\d+)", summary)], evidence["refs"])
            self.assertNotRegex(summary, r"(?i)\b(?:fixes|resolves)\s+#")

    def test_material_caveats_remain_visible(self):
        cases = {case["name"]: case for case in self.examples["cases"]}
        failed = cases["failed-unrun-stale"]
        for phrase in ("not ready to merge", "duplicate bytes", "not run", "stale", "renew review"):
            self.assertIn(phrase, failed["summary"])
        self.assertIn("failed", failed["evidence"]["checks"]["large_file"])
        migration = cases["migration"]
        for phrase in ("incompatible", "not been exercised", "maintainer", "backup, conversion, then restart", "Reverting source alone"):
            self.assertIn(phrase, migration["summary"])
        self.assertEqual(migration["evidence"]["checks"]["backup_restore"], "not run")


if __name__ == "__main__":
    unittest.main()
