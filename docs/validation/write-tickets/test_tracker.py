"""Executed authored fixture decisions, not autonomous agent compliance."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

from tracker_fixture import FakeTracker

REPO = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location(
    "dependencies", REPO / "workflow/setup-project/scripts/dependencies.py")
dependencies = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dependencies)


class PersistedTicketTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "state.json"
        self.api = FakeTracker(self.path)
        for title, labels in (("Spec", ["spec", "area-a"]),
                              ("Design", ["implementation-step", "area-a"]),
                              ("Build", ["implementation-step", "area-a"]),
                              ("Check", ["implementation-step", "area-a"])):
            self.api.create(title, "AC1: observable result; protected existing behavior", labels)
        self.plan = {"repository": "example/project", "dependencies": [
            {"blocked": 3, "by": 2}, {"blocked": 4, "by": 3}]}

    def parent(self, parent, child):
        self.api.request(f"{parent}/sub_issues", "POST", {"sub_issue_id": 9000 + child})

    def test_persisted_graph_both_directions_and_clean_rerun(self):
        for child in (2, 3, 4):
            self.parent(1, child)
        report = dependencies.reconcile(self.plan, self.api, apply=True)
        self.assertEqual(report["added"], 2)
        # Reopen the disk store: proof is actual persisted state, not body prose.
        api = FakeTracker(self.path)
        children = api.request("1/sub_issues", paginated=True)
        self.assertEqual([i["id"] for i in children], [9002, 9003, 9004])
        for child in (2, 3, 4):
            self.assertEqual(api.request(f"{child}/parent")["id"], 9001)
        for blocked, by in ((3, 2), (4, 3)):
            self.assertEqual(api.request(f"{blocked}/dependencies/blocked_by", paginated=True)[0]["id"], 9000 + by)
            self.assertEqual(api.request(f"{by}/dependencies/blocking", paginated=True)[0]["id"], 9000 + blocked)
        self.assertIn(("1/sub_issues", 3), api.pages)
        before = self.path.read_bytes()
        self.assertEqual(dependencies.reconcile(self.plan, api, apply=True)["added"], 0)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertFalse(any(method == "POST" for _, method, _, _ in api.calls))
        self.assertTrue(all("area-a" in i["labels"] and "ready-for-agent" not in i["labels"]
                            for i in api.load()["issues"]))

    def test_blocker_pagination_preserves_unrelated_edges(self):
        self.api.request("4/dependencies/blocked_by", "POST", {"issue_id": 9002})
        dependencies.reconcile(self.plan, self.api, apply=True)
        self.assertEqual(self.api.load()["blockers"]["4"], [2, 3])
        self.assertIn(("4/dependencies/blocked_by", 2), self.api.pages)
        self.assertIn(("2/dependencies/blocking", 2), self.api.pages)

    def test_combined_blocker_cycle_stops_before_writes(self):
        self.api.request("2/dependencies/blocked_by", "POST", {"issue_id": 9004})
        before = self.path.read_bytes()
        with self.assertRaises(dependencies.Blocked):
            dependencies.reconcile(self.plan, self.api, apply=True)
        self.assertEqual(self.path.read_bytes(), before)

    def test_parent_conflict_and_ancestry_cycle_preserve_state(self):
        self.parent(2, 3)
        before = self.path.read_bytes()
        with self.assertRaisesRegex(ValueError, "conflicting parent"):
            self.parent(1, 3)
        with self.assertRaisesRegex(ValueError, "hierarchy cycle"):
            self.parent(3, 2)
        self.assertEqual(self.path.read_bytes(), before)

    def test_number_is_not_database_id(self):
        before = self.path.read_bytes()
        with self.assertRaisesRegex(ValueError, "database ID"):
            self.api.request("1/sub_issues", "POST", {"sub_issue_id": 3})
        self.assertEqual(self.path.read_bytes(), before)

    def test_wrong_readback_id_blocks_after_persistence(self):
        for suffix in ("3/dependencies/blocked_by", "2/dependencies/blocking"):
            with self.subTest(suffix=suffix):
                self.api.save({"issues": self.api.load()["issues"], "parents": {}, "blockers": {}})
                self.api.wrong_id = suffix
                with self.assertRaisesRegex(dependencies.Blocked, "Database ID mismatch"):
                    dependencies.reconcile(self.plan, self.api, apply=True)
                self.assertEqual(self.api.load()["blockers"], {"3": [2]})

    def test_failed_parent_readback_is_unknown_not_absence(self):
        self.parent(1, 3)
        self.api.fail = "3/parent"
        with self.assertRaisesRegex(RuntimeError, "unavailable"):
            self.api.request("3/parent")
        self.assertEqual(self.api.load()["parents"], {"3": 1})
        self.api.fail = None
        self.assertEqual(self.api.request("3/parent")["id"], 9001)

    def test_partial_blocker_write_inspected_before_retry(self):
        self.api.timeout_after_write = True
        with self.assertRaisesRegex(RuntimeError, "timeout"):
            dependencies.reconcile(self.plan, self.api, apply=True)
        self.assertEqual(self.api.load()["blockers"], {"3": [2]})
        api = FakeTracker(self.path)
        self.assertEqual(dependencies.reconcile(self.plan, api, apply=True)["added"], 1)
        self.assertEqual([c[2] for c in api.calls if c[1] == "POST"], [{"issue_id": 9003}])

    def test_creation_timeout_duplicate_search_and_standalone_bug(self):
        self.api.timeout_after_write = True
        with self.assertRaisesRegex(RuntimeError, "timeout"):
            self.api.create("Bug: stale export", "Expected/actual; reproduced cause; regression check", ["bug", "area-a"])
        api = FakeTracker(self.path)
        # Authored caller decision: reconcile matching identity rather than re-create.
        matches = [i for i in api.load()["issues"] if i["title"] == "Bug: stale export"]
        self.assertEqual(len(matches), 1)
        actual = api.request(str(matches[0]["number"]))
        self.assertEqual(actual["labels"], ["bug", "area-a"])
        self.assertIsNone(api.request(f'{actual["number"]}/parent'))
        self.assertEqual(len(api.load()["issues"]), 5)
        api.create(actual["title"], actual["body"], actual["labels"])
        before = self.path.read_bytes()
        matches = [i for i in api.load()["issues"] if i["title"] == actual["title"]]
        self.assertEqual(len(matches), 2)  # Ambiguous: caller stops without another write.
        self.assertEqual(self.path.read_bytes(), before)

    def test_readiness_survives_blockage_but_does_not_enable_scheduling(self):
        # Authored classifications, not an executable readiness policy engine.
        for actor in ("agent", "human"):
            for blocked in (False, True):
                with self.subTest(actor=actor, blocked=blocked):
                    issue = self.api.create("Actionable next work", "AC1: defined next action",
                                            ["implementation-step", "area-a"])
                    number = issue["number"]
                    self.parent(1, number)
                    if blocked:
                        self.api.request(f"{number}/dependencies/blocked_by", "POST",
                                         {"issue_id": 9002})
                    graph_before = self.api.load()
                    expected = issue["labels"] + [f"ready-for-{actor}"]
                    self.api.request(str(number), "PATCH", {"labels": expected})
                    api = FakeTracker(self.path)
                    actual = api.request(str(number))
                    self.assertEqual(actual["labels"], expected)
                    self.assertEqual(api.load()["parents"], graph_before["parents"])
                    self.assertEqual(api.load()["blockers"], graph_before["blockers"])
                    blockers = api.request(f"{number}/dependencies/blocked_by", paginated=True)
                    # Authored scheduling gate: ready alone cannot clear open prerequisites.
                    eligible = actor == "agent" and not blockers
                    self.assertEqual(eligible, actor == "agent" and not blocked)

    def test_blocked_specs_keep_next_actor_readiness_and_existing_edges(self):
        for actor in ("agent", "human"):
            issue = self.api.create("Parent agreement", "Actionable coordination or human decision",
                                    ["spec", "area-a", f"ready-for-{actor}"])
            number = issue["number"]
            self.api.request(f"{number}/dependencies/blocked_by", "POST", {"issue_id": 9002})
            api = FakeTracker(self.path)
            self.assertEqual(api.request(str(number))["labels"],
                             ["spec", "area-a", f"ready-for-{actor}"])
            self.assertEqual(api.request(f"{number}/dependencies/blocked_by", paginated=True)[0]["id"], 9002)
            # A ready parent is a coordination entry, not another implementation unit.
            self.assertNotIn("implementation-step", api.request(str(number))["labels"])
            self.assertEqual(api.request(f"{number}/sub_issues", paginated=True), [])

    def test_label_readback_failure_preserves_unknown_write_for_inspection(self):
        before = self.api.load()
        expected = before["issues"][2]["labels"] + ["ready-for-agent"]
        self.api.timeout_after_write = True
        with self.assertRaisesRegex(RuntimeError, "timeout"):
            self.api.request("3", "PATCH", {"labels": expected})
        self.api.fail = "3"
        with self.assertRaisesRegex(RuntimeError, "unavailable"):
            self.api.request("3")
        # No verified assignment claimed; reopen and inspect before retrying.
        api = FakeTracker(self.path)
        self.assertEqual(api.request("3")["labels"], expected)
        self.assertEqual(api.load()["parents"], before["parents"])
        self.assertEqual(api.load()["blockers"], before["blockers"])
        self.assertEqual(api.calls, [("3", "GET", None, False)])

    def test_missing_deciding_evidence_does_not_fabricate_fix_readiness(self):
        issue = self.api.create("Unconfirmed symptom", "Cause unknown; diagnostic scope undecided",
                                ["bug", "needs-info"])
        actual = FakeTracker(self.path).request(str(issue["number"]))
        self.assertEqual(actual["labels"], ["bug", "needs-info"])
        self.assertNotIn("ready-for-agent", actual["labels"])

    def test_missing_label_authority_retains_proposal_without_mutation(self):
        before = self.path.read_bytes()
        actual = self.api.request("3")
        proposed = actual["labels"] + ["ready-for-agent"]
        self.assertNotEqual(proposed, actual["labels"])
        # This authored caller has inspection authority only, so it returns the delta.
        self.assertEqual(self.api.calls, [("3", "GET", None, False)])
        self.assertEqual(self.path.read_bytes(), before)

    def test_plan_only_has_no_writes_or_ready_assignments(self):
        before = self.path.read_bytes()
        self.assertEqual(dependencies.reconcile(self.plan, self.api)["status"], "planned")
        self.assertEqual(self.path.read_bytes(), before)
        self.assertFalse(any(method == "POST" for _, method, _, _ in self.api.calls))
        self.assertTrue(all("ready-for-agent" not in i["labels"] for i in self.api.load()["issues"]))


if __name__ == "__main__":
    unittest.main()
