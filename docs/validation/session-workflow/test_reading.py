"""Check reading arithmetic and route membership, not instruction adherence."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location(
    "reading", ROOT / "docs/validation/session-delivery/measure_reading.py")
reading = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reading)


class Reading(unittest.TestCase):
    def test_selected_ticket_includes_current_adapter(self):
        scenarios = reading.manifests(False)
        ticket = scenarios["investigation_selected_ticket"]["investigator"]
        self.assertIn(reading.ref("investigate-bug", "ticket-stage"), ticket)
        self.assertIn(reading.ref("setup-project", "native-tracker"), ticket)
        self.assertNotIn(reading.entry("setup-project"), ticket)
        self.assertNotIn(reading.ref("setup-project", "issue-tracker"), ticket)
        baseline = reading.manifests(True)["investigation_selected_ticket"]["investigator"]
        self.assertTrue(set(reading.OLD_TRACKER).issubset(baseline))
        diagnosis = scenarios["investigation_diagnosis_only"]["investigator"]
        self.assertEqual(diagnosis, [reading.entry("investigate-bug")])

    def test_equivalent_published_endpoint_keeps_PR(self):
        for historical in (True, False):
            scenarios = reading.manifests(historical)
            lead = scenarios["bounded_delivery_with_PR"]["lead"]
            self.assertTrue(set(reading.PR).issubset(lead))
            # Independent explicit paths catch policy omissions even if PR itself
            # is accidentally shortened. Required for report and publication.
            for policy in ("docs/agents/issue-tracker.md", "docs/agents/triage-labels.md"):
                self.assertIn(policy, lead)
                self.assertIn(policy, scenarios["selected_PR_fresh_context"]["publisher"])
            self.assertFalse(set(reading.PR) & set(scenarios["bounded_delivery_before_PR"]["lead"]))
            for axis in ("standards", "spec"):
                self.assertEqual(scenarios["bounded_delivery_with_PR"][axis], reading.REVIEW)

    def test_full_files_per_context_and_actual_project_cost(self):
        result = reading.measure("45e5a24")
        for revision in result["observations"].values():
            for scenario in revision.values():
                for kind in ("fixed", "actual"):
                    key = kind + "_project_total"
                    self.assertEqual(scenario[key], sum(c[key] for c in scenario["contexts"].values()))
                    for context in scenario["contexts"].values():
                        self.assertEqual(context[key], sum(context["instruction_paths"].values())
                                         + sum(context[kind + "_project_paths"].values()))
        candidate = result["observations"]["candidate"]["bounded_delivery_with_PR"]
        for axis in ("standards", "spec"):
            self.assertEqual(candidate["contexts"][axis]["fixed_project_paths"],
                             candidate["contexts"]["lead"]["fixed_project_paths"])
        for kind in ("fixed", "actual"):
            comparisons = result["comparisons_with_" + kind + "_project"]
            for row in comparisons.values():
                self.assertEqual(row["reduction_words"], row["baseline"] - row["candidate"])
        # WF-11's three equivalent complete outcomes must improve with actual
        # common guidance charged, not only when project documents are held fixed.
        for scenario in ("planning", "investigation_selected_ticket", "bounded_delivery_with_PR"):
            self.assertGreater(result["comparisons_with_actual_project"][scenario]["reduction_words"], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
