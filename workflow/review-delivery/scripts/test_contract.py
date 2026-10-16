#!/usr/bin/env python3
"""Portable source guards, not independent-review behavior trials."""
from pathlib import Path
import unittest

PACKAGE = Path(__file__).resolve().parents[1]


class ReviewContract(unittest.TestCase):
    def test_project_and_retention_boundaries(self):
        entry = (PACKAGE / "SKILL.md").read_text()
        for clause in ("meaningful project agreement", "regardless of filenames",
                       "specific reconciliation recommendation", "Same-session evidence may remain in conversation",
                       "active owners, uncertain effects and spent allowances"):
            self.assertIn(clause, entry)
        scope = (PACKAGE / "references/scope.md").read_text()
        self.assertIn("not a mandatory ledger, durable report or state service", scope)

    def test_delegation_does_not_load_delivery_for_policy(self):
        handoff = (PACKAGE / "references/handoff.md").read_text()
        for clause in ("conditional library pointer", "not the unrelated delivery procedure or universal policy contract",
                       "old universal-contract-only package", "ticket workers request reviewer assignments",
                       "No delivery companion or new ledger is needed for plain direct inspection"):
            self.assertIn(clause, handoff)
        self.assertNotIn("Read its complete entry and execution/handoff contract", handoff)

    def test_independence_neutrality_and_freshness_remain(self):
        report = (PACKAGE / "references/report.md").read_text()
        scope = (PACKAGE / "references/scope.md").read_text()
        entry = (PACKAGE / "SKILL.md").read_text()
        for clause in ("neither receives the other's conclusions", "prior reviewer verdicts",
                       "ineligible", "blocking", "original axis report"):
            self.assertIn(clause.lower(), report.lower())
        self.assertIn("Newly relevant files", scope)
        self.assertIn("index/staged/unstaged fingerprints", scope)
        self.assertIn("relevant untracked files", scope)
        self.assertIn("lead self-review", entry.lower())
        self.assertIn("Material unresolved findings block delivery acceptance", entry)


if __name__ == "__main__":
    unittest.main(verbosity=2)
