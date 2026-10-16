#!/usr/bin/env python3
"""Offline instruction guards; not agent execution or hosted PR validation."""
from pathlib import Path
import unittest

PACKAGE = Path(__file__).resolve().parents[1]


class ReportingContract(unittest.TestCase):
    def test_project_owned_guidance_and_selected_effects(self):
        entry = (PACKAGE / "SKILL.md").read_text()
        for clause in ("meaningful project agreement", "regardless of filenames",
                       "specific reconciliation recommendation", "explicit compound request",
                       "alone does not select PR preparation/publication",
                       "Same-session evidence can remain in conversation",
                       "If publication is unrequested"):
            self.assertIn(clause, entry)
        self.assertIn("active owners, uncertain effects or spent allowances", entry)

    def test_conditional_library_and_reused_evidence(self):
        entry = (PACKAGE / "SKILL.md").read_text()
        for clause in ("conditional coordination library", "not its delivery procedure or universal contract",
                       "Reuse current complete evidence", "does not repair", "Lead inspection is not independent review",
                       "Material unresolved findings", "merge, closure"):
            self.assertIn(clause, entry)
        self.assertNotIn("consume the discovered `work-on` execution library", entry)

    def test_publication_inspects_actual_effects(self):
        publication = (PACKAGE / "references/publication.md").read_text()
        for clause in ("requested and permitted", "Report-only requests perform zero remote writes",
                       "After a timeout/partial failure, inspect actual remote state before retrying",
                       "read-back", "no automatic merge"):
            self.assertIn(clause, publication)


if __name__ == "__main__":
    unittest.main(verbosity=2)
