"""Selected-stage regression examples, not a skill executor or agent trial.

Caller decisions and concise returns are authored examples. Actual JSON fixture
writes/read-back exercise persistence; text checks guard instruction boundaries.
Run: python3 -B -m unittest discover -s docs/validation/discovery-spec-tickets -p 'test_*.py'
"""
import importlib.util
from pathlib import Path
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
spec = importlib.util.spec_from_file_location(
    "selected_stage_tracker", REPO / "docs/validation/write-tickets/tracker_fixture.py")
fixture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixture)


class SelectedStageExamples(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.api = fixture.FakeTracker(Path(self.temp.name) / "tracker.json")
        self.body = (HERE / "spec.md").read_text()

    def instruction(self, package):
        return (REPO / "workflow" / package / "SKILL.md").read_text()

    def test_confirmed_plan_is_terminal_without_storage_or_next_stage(self):
        text = self.instruction("shape-work")
        self.assertIn("A confirmed plan completes shaping", text)
        self.assertIn("even if the user creates no further artifact", text)
        self.assertNotIn("multi-session work needs an approved durable pointer", text)
        self.assertIn("without starting it", text)
        # Authored owner turn: "The plan is right; stop here."
        self.assertEqual(self.api.load()["issues"], [])
        self.assertEqual(self.api.calls, [])

    def test_agreed_plan_publication_has_link_return_not_full_body(self):
        text = self.instruction("write-spec")
        self.assertIn("invoking `/write-spec` on an agreed plan selects", text)
        self.assertIn("Do not paste the full spec", text)
        self.assertNotIn("Default to authorized inspection and a conversation draft", text)
        # Authored configured command; no additional prose-approval turn.
        issue = self.api.create("Reading list specification", self.body, ["spec"])
        actual = self.api.request(str(issue["number"]))
        self.assertEqual(actual["body"], self.body)
        self.assertEqual(actual["labels"], ["spec"])
        response = "[Spec #1](https://example.invalid/project/issues/1) — Reading list behavior."
        self.assertNotIn(self.body, response)
        self.assertEqual(len(self.api.load()["issues"]), 1)
        self.assertEqual(self.api.load()["parents"], {})
        self.assertNotIn("ready-for-agent", actual["labels"])

    def test_explicit_draft_local_review_overrides_have_zero_writes(self):
        for package in ("write-spec", "write-tickets"):
            text = self.instruction(package)
            self.assertIn("review-only requests override", text)
            self.assertNotIn("A multi-session handoff needs an approved durable pointer", text)
        before = self.api.path.read_bytes()
        # Three authored explicit modes; the caller never invokes create/POST.
        for mode in ("draft", "local-only", "review-only"):
            with self.subTest(mode=mode):
                self.assertEqual(self.api.path.read_bytes(), before)
                self.assertEqual(self.api.calls, [])

    def test_ticket_table_uses_verified_ids_not_full_bodies(self):
        text = self.instruction("write-tickets")
        self.assertIn("table of linked ticket numbers/IDs and short descriptions", text)
        self.assertIn("agent owns decomposition and full ticket wording", text)
        self.assertNotIn("exact titles/bodies and label deltas", text)
        parent = self.api.create("Spec", self.body, ["spec", "area-a"])
        rows = []
        for title in ("Pin selected books", "Verify pin recovery"):
            body = "P1–P3: " + title + "; preserve reader filtering and input order."
            child = self.api.create(title, body, ["implementation-step", "area-a"])
            self.api.request("1/sub_issues", "POST", {"sub_issue_id": child["id"]})
            read = self.api.request(str(child["number"]))
            self.assertEqual(read["body"], body)
            self.assertEqual(self.api.request(f'{child["number"]}/parent')["id"], parent["id"])
            rows.append(f'| [#{read["number"]}](https://example.invalid/project/issues/{read["number"]}) | {title} |')
        children = self.api.request("1/sub_issues", paginated=True)
        self.assertEqual([c["number"] for c in children], [2, 3])
        self.assertIn(("1/sub_issues", 2), self.api.pages)
        response = "| Ticket | Description |\n| --- | --- |\n" + "\n".join(rows)
        self.assertIn("[#2]", response)
        self.assertIn("[#3]", response)
        self.assertNotIn("P1–P3:", response)
        self.assertTrue(all("ready-for-agent" not in i["labels"] for i in children))

    def test_partial_creation_is_reconciled_without_second_create(self):
        self.api.timeout_after_write = True
        with self.assertRaisesRegex(RuntimeError, "timeout"):
            self.api.create("Spec", self.body, ["spec"])
        api = fixture.FakeTracker(self.api.path)
        matches = [i for i in api.load()["issues"] if i["body"] == self.body and i["labels"] == ["spec"]]
        self.assertEqual(len(matches), 1)
        self.assertEqual(api.request(str(matches[0]["number"]))["body"], self.body)
        self.assertEqual(len(api.load()["issues"]), 1)
        self.assertFalse(any(c[1] == "POST" for c in api.calls))

    def test_unknown_graph_blocks_claim_without_mutation(self):
        issue = self.api.create("Spec", self.body, ["spec"])
        self.api.fail = f'{issue["number"]}/sub_issues'
        before = self.api.path.read_bytes()
        with self.assertRaisesRegex(RuntimeError, "unavailable"):
            self.api.request(self.api.fail, paginated=True)
        self.assertEqual(self.api.path.read_bytes(), before)
        for package in ("shape-work", "write-spec", "write-tickets"):
            text = self.instruction(package)
            self.assertIn("once per context", text)
            self.assertIn("Missing common guidance blocks", text)
            self.assertIn("conditional coordination library", text)


if __name__ == "__main__":
    unittest.main()
