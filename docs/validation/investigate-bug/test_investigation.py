"""Authored offline investigation cases, not an agent or production workflow engine."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "ticket_fixture", ROOT / "docs/validation/write-tickets/tracker_fixture.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
FakeTracker = MODULE.FakeTracker

BUG = "def total(prices, discount):\n    return sum(prices) - discount\n"
CALLER = "prices = [40, 60]; discount = 0.10\n"
EXPECTATION = "Discount is a fraction of the subtotal; 100 at 10% costs 90."


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class InvestigationCases(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.home = Path(self.tmp.name)
        self.product = self.home / "pricing.py"
        self.product.write_text(BUG)
        self.caller = self.home / "caller.py"
        self.caller.write_text(CALLER)
        self.unrelated = self.home / "private-work.txt"
        self.unrelated.write_text("protected partial work\n")
        self.original = {p: p.read_bytes() for p in
                         (self.product, self.caller, self.unrelated)}
        self.tracker = FakeTracker(self.home / "tracker.json")

    def observe(self, discount=0.10):
        namespace = {}
        exec(compile(self.product.read_text(), "pricing.py", "exec"), namespace)
        return namespace["total"]([40, 60], discount)

    def evidence(self):
        actual = self.observe()
        self.assertEqual(actual, 99.9)
        # Discriminating observations: the amount deducted equals the raw fraction,
        # not fraction times subtotal; inspect the exact source above as support.
        self.assertEqual(self.observe(0), 100)
        self.assertEqual(self.observe(0.20), 99.8)
        return {
            "kind": "implementation-ready", "expected": 90, "actual": actual,
            "agreement": EXPECTATION, "impact": "Customer overcharged by 9.90",
            "environment": "Python " + sys.version.split()[0] + ", isolated synthetic pricing module",
            "reproduction": "total([40, 60], 0.10)",
            "observations": [99.9, 100, 99.8], "attempts": 3,
            "cause": "pricing.py:2 subtracts fraction directly instead of subtotal * fraction",
            "inputs": {"pricing.py": digest(self.product), "caller.py": digest(self.caller)},
            "fix_scope": "Apply fractional discount to subtotal in total()",
            "constraints": "Keep caller fraction contract and public signature",
            "exclusions": "No rounding, currency, tax or API redesign",
            "dependencies": [], "risks": "Check zero discount and empty subtotal",
            "acceptance": {"R1": "100 at 10% returns 90", "R2": "Zero discount returns subtotal"},
            "regression": "Assert R1 fails with 99.9 on pinned source, retain R2 control",
            "method": "tdd: deterministic behavior with existing callable seam",
            "uncertainty": "Synthetic arithmetic only; no production rounding claim",
            "artifacts": "No probes created; inline reproduction retained in ticket",
        }

    def publish(self, title, evidence):
        # Exact local fixture publication is an authored test decision, not a
        # permission detector. No role/readiness label or parent is invented.
        issue = self.tracker.create(title, json.dumps(evidence, sort_keys=True), ["bug"])
        readback = self.tracker.request(str(issue["number"]))
        self.assertEqual(readback, issue)
        self.assertEqual(json.loads(readback["body"]), evidence)
        self.assertEqual(self.tracker.load()["parents"], {})
        self.assertEqual(self.tracker.load()["blockers"], {})
        self.assertNotIn("ready-for-agent", readback["labels"])
        return readback

    def unchanged(self):
        for path, content in self.original.items():
            self.assertEqual(path.read_bytes(), content)

    def test_confirmed_ticket_probe_cleanup_and_investigation_only_stop(self):
        evidence = self.evidence()
        original = self.product.read_bytes()
        probe = "\n# owned diagnostic marker, no repair\n"
        self.product.write_text(BUG + probe)
        self.assertEqual(self.observe(), 99.9)
        self.product.write_bytes(original)  # only owned edit, no concurrent changes
        repro = self.home / "reproduction.py"
        repro.write_text("from pricing import total\nassert total([40, 60], .10) == 90\n")
        result = subprocess.run([sys.executable, "reproduction.py"], cwd=self.home,
                                capture_output=True, text=True, timeout=5)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("AssertionError", result.stderr)
        evidence["artifacts"] = "Owned probe restored; reproduction.py retained in scratch home"
        evidence["reproduction_artifact"] = {
            "command": "python3 reproduction.py", "exit_code": result.returncode,
            "failure": "AssertionError", "product_digest": digest(self.product)}
        ticket = self.publish("Fractional discount overcharges customers", evidence)
        self.assertEqual(json.loads(ticket["body"])["kind"], "implementation-ready")
        self.assertTrue(repro.exists())
        self.unchanged()  # original remains defective: no fix/automatic delivery

    def test_intermittent_observed_but_cause_unresolved(self):
        # Explicit scheduled synthetic trigger; not random or real intermittency.
        observations = [self.observe(0), self.observe(.10), self.observe(0)]
        self.assertEqual(observations, [100, 99.9, 100])
        evidence = {"kind": "investigation-only", "attempts": 3,
                    "failures": 1, "successes": 2, "observations": observations,
                    "trigger": "Fixture alternates zero/10%/zero inputs",
                    "blocker": "Reported caller's reason for alternating input unknown",
                    "next_action": "Capture caller input in approved environment"}
        self.publish("Investigate intermittent discount report", evidence)
        self.unchanged()

    def test_unconfirmed_and_harness_failure_not_bug_confirmation(self):
        observations = [self.observe(0) for _ in range(3)]
        self.assertEqual(observations, [100] * 3)
        with self.assertRaises(TypeError):
            self.observe(None)
        self.publish("Investigate unconfirmed discount report", {
            "kind": "investigation-only", "attempts": 3, "observations": observations,
            "blocker": "Reported failing inputs unavailable; None probe is harness error",
            "next_action": "Obtain safe failing input and environment",
            "cause": None})
        self.unchanged()

    def test_confirmed_unresolved_cause_remains_investigation(self):
        self.assertEqual(self.observe(), 99.9)
        # Withhold implementation inspection to model a bounded access gap.
        self.publish("Investigate discount arithmetic discrepancy", {
            "kind": "investigation-only", "expected": 90, "actual": 99.9,
            "cause": None, "blocker": "Deciding source unavailable to this case",
            "acceptance": "Inspect deciding source and explain observed discrepancy",
            "next_action": "Request bounded source access, not a speculative fix"})
        self.unchanged()

    def test_duplicate_reconciles_existing_issue_without_new_hierarchy(self):
        evidence = self.evidence()
        existing = self.tracker.create("Discount defect", json.dumps(evidence), ["bug", "needs-info"])
        state = self.tracker.load()
        # Match inspected symptom, contract, cause and input identities, not title.
        matches = [i for i in state["issues"]
                   if json.loads(i["body"])["inputs"] == evidence["inputs"]
                   and json.loads(i["body"])["cause"] == evidence["cause"]]
        self.assertEqual([i["id"] for i in matches], [existing["id"]])
        updated = dict(evidence, reconciliation="Current reproduction reconfirmed")
        state["issues"][0]["body"] = json.dumps(updated)
        self.tracker.save(state)  # exact authored body-only update
        readback = self.tracker.request(str(existing["number"]))
        self.assertEqual(json.loads(readback["body"]), updated)
        self.assertEqual(readback["labels"], existing["labels"])
        self.assertEqual(len(self.tracker.load()["issues"]), 1)
        self.unchanged()

    def test_current_handoff_reused_without_new_diagnosis(self):
        evidence = self.evidence()
        ticket = self.publish("Discount defect", evidence)
        current = {"pricing.py": digest(self.product), "caller.py": digest(self.caller)}
        self.assertEqual(current, json.loads(ticket["body"])["inputs"])
        # Receiver reads source and pinned evidence; no new observe(), Analyze or fix.
        self.assertIn("sum(prices) - discount", self.product.read_text())
        self.assertEqual(evidence["method"].split(":")[0], "tdd")
        self.unchanged()

    def test_dirty_caller_change_invalidates_only_dependent_evidence(self):
        evidence = self.evidence()
        ticket = self.publish("Discount defect", evidence)
        self.caller.write_text("prices = [40, 60]; discount = 10\n")
        self.assertEqual(digest(self.product), evidence["inputs"]["pricing.py"])
        self.assertNotEqual(digest(self.caller), evidence["inputs"]["caller.py"])
        # Targeted new observation: changed caller now reproduces expected 90;
        # old caller/cause applicability cannot be claimed for this state.
        self.assertEqual(self.observe(10), 90)
        revised = dict(evidence, kind="investigation-only",
                       stale=["caller reproduction", "cause applicability", "fix scope"],
                       next_action="Reconcile changed caller unit contract")
        self.assertEqual(revised["agreement"], evidence["agreement"])
        self.assertEqual(revised["impact"], evidence["impact"])
        self.assertEqual(json.loads(ticket["body"]), evidence)  # old-state history retained
        self.assertEqual(self.product.read_bytes(), self.original[self.product])
        self.assertEqual(self.unrelated.read_bytes(), self.original[self.unrelated])


if __name__ == "__main__":
    unittest.main()
