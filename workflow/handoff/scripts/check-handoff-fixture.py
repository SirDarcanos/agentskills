#!/usr/bin/env python3
"""Offline instruction assertions and disposable storage/transfer examples.

Authored examples are not agent lifecycle, routing or recovery evidence.
"""
import json
import os
from pathlib import Path
import tempfile
import unittest

PACKAGE = Path(__file__).resolve().parents[1]


class Handoff(unittest.TestCase):
    def test_invocation_and_receiving_authority(self):
        entry = (PACKAGE / "SKILL.md").read_text()
        for clause in ("disable-model-invocation: true", "only when the user explicitly requests",
                       "Without that user request, stop", "not authorize it",
                       "Design-only handoffs need none", "Do not assume access to an earlier session",
                       "pre-existing durable record is not a handoff prerequisite",
                       "Missing history stays an explicit recovery gap",
                       "State-description can still capture inspected facts"):
            self.assertIn(clause, entry)
        self.assertNotIn("references/contracts.md", entry)
        self.assertNotIn("../work-on/", entry)

    def test_explicit_transfer_readback_and_no_overwrite(self):
        # Explicit synthetic destination, never a user's workspace or tracker.
        with tempfile.TemporaryDirectory(prefix="handoff-fixture-") as directory:
            destination = Path(directory) / "selected.md"
            state = {"purpose": "continue bounded delivery", "authority": "inspect only",
                     "integrated": ["A"], "not_integrated": ["B"],
                     "owner": {"B": "uncertain"}, "spent": 2,
                     "remote_effect": "unknown; inspect before retry"}
            content = "# Selected continuation\n\n" + json.dumps(state, sort_keys=True) + "\n"
            fd = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd, "w") as output:
                output.write(content)
            self.assertEqual(destination.read_text(), content)
            if os.name == "posix":
                self.assertEqual(destination.stat().st_mode & 0o777, 0o600)
            with self.assertRaises(FileExistsError):
                os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            # Fresh synthetic receiver gets only saved content, not prior context.
            received = json.loads(destination.read_text().split("\n\n", 1)[1])
            self.assertEqual(received, state)
            self.assertEqual(received["spent"], 2)
            self.assertEqual(received["owner"]["B"], "uncertain")
            self.assertEqual(received["authority"], "inspect only")
            self.assertNotIn("resumed", received)

    def test_absent_history_and_shaping_transfer(self):
        # Missing data stays unknown; shaping does not acquire delivery machinery.
        shaping = {"purpose": "finish shaping", "decisions": ["bounded outcome"],
                   "questions": ["confirm scope"], "next_authority": "unconfirmed"}
        self.assertNotIn("ledger", shaping)
        self.assertIsNone(shaping.get("spent"))
        self.assertIsNone(shaping.get("workers"))
        entry = (PACKAGE / "SKILL.md").read_text()
        self.assertIn("conversation-only draft with the storage gap", entry)
        self.assertIn("inspect before retrying", entry)


if __name__ == "__main__":
    unittest.main(verbosity=2)
