"""Authored publication examples using persisted CRUD, not agent-adherence tests."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


class SpecReadinessExamples(unittest.TestCase):
    def test_agent_and_human_spec_creation_and_failed_label_readback(self):
        for actor in ("agent", "human"):
            with self.subTest(actor=actor), tempfile.TemporaryDirectory() as temp:
                store = Path(temp) / "state.json"
                command = [sys.executable, "-B", str(HERE / "tracker_fixture.py"), str(store)]
                labels = ["spec", "area-a", f"ready-for-{actor}"]
                # Keep this positive input separate from the design-unready spec.md.
                body = Path(temp) / "actionable-spec.md"
                next_action = (
                    "Approved behavior and shared design are settled. Acceptance is checkable; "
                    "dependencies are known. The agent's next action is coordinating eligible children, "
                    "not implementing the parent again."
                    if actor == "agent" else
                    "The defined next action is a human decision: choose whether spreadsheet export "
                    "includes private notes. Implementation readiness is withheld pending that decision."
                )
                body.write_text(
                    "# Reading list agreement\n\n"
                    "AC1: A requested export contains visible list titles.\n\n"
                    + next_action + "\n\n"
                    "Fixture policy maps the spec role to spec, agent readiness to ready-for-agent "
                    "and human readiness to ready-for-human. The fixture owner authorizes local "
                    "publication with the justified next-actor label and area-a; no live tracker writes "
                    "or scheduling are authorized.\n"
                )
                subprocess.run(command + ["create", "--title", "Reading list agreement",
                               "--body", str(body), "--labels", *labels],
                               check=True, capture_output=True, text=True)
                read = subprocess.run(command + ["read", "--number", "1"],
                                      check=True, capture_output=True, text=True)
                actual = json.loads(read.stdout)
                self.assertEqual(actual["labels"], labels)
                self.assertEqual(actual["body"], body.read_text())
                self.assertNotIn("implementation-step", actual["labels"])
                self.assertEqual(actual["relationships"], [])
                before = store.read_bytes()
                failed = subprocess.run(command + ["read", "--number", "1", "--fail-read"],
                                        capture_output=True, text=True)
                self.assertNotEqual(failed.returncode, 0)
                self.assertIn("unavailable", failed.stderr)
                self.assertEqual(store.read_bytes(), before)

    def test_instructions_require_assignment_not_just_optional_assessment(self):
        tickets = (REPO / "workflow/write-tickets/SKILL.md").read_text()
        publication = (REPO / "workflow/write-spec/references/publication.md").read_text()
        for text in (tickets, publication):
            self.assertIn("mapped agent-ready label", text)
            self.assertIn("mapped human-ready label", text)
            self.assertIn("without redundant confirmation", text)
            self.assertIn("native blocker/completion checks", text)
        self.assertIn("equivalent blocked and unblocked work", tickets)
        self.assertNotIn("Publication never automatically adds readiness", tickets)
        self.assertIn("alongside the spec role", publication)
        self.assertIn("Native blockers alone neither suppress readiness", publication)
        self.assertIn("not duplicate parent implementation", publication)


if __name__ == "__main__":
    unittest.main()
