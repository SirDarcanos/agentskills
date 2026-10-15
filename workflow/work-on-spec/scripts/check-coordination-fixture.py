#!/usr/bin/env python3
"""Offline synthetic coordination assertions and real local Git tools.

Not a scheduler, tracker adapter, agent runner or acceptance engine. Fixture
choices are authored; assertions do not demonstrate autonomous instruction use.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

PACKAGE = Path(__file__).resolve().parents[1]


def fingerprint(root):
    return {name: hashlib.sha256((root / name).read_bytes()).hexdigest()
            for name in ("core.py", "consumer.py", "check.py")}


class Coordination(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="work-on-spec-fixture-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        # Synthetic native observations, not a graph/API implementation.
        self.graph = {"parent": {key: "P" for key in "ABCD"},
                      "blocked_by": {"A": [], "B": [], "C": ["A"], "D": []}}
        self.roles = {"P": "spec", **{key: "work" for key in "ABCD"}}
        self.owned = {"A": {"core.py"}, "B": {"core.py"},
                      "C": {"consumer.py"}, "D": {"docs.md"}}
        self.ledger = {"run": "fixture-root", "active": [],
                       "checkpoints": {"local-A": {"cause": "normalization", "spent": 2},
                                       "aggregate": {"spent": 0}},
                       "model": {"reserved": 1, "attempted": 1, "unknown_charge": True}}
        self.original_graph = json.dumps(self.graph, sort_keys=True)

    def git(self, *args):
        env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        env.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1")
        result = subprocess.run(["git", "-c", f"core.hooksPath={os.devnull}",
                                 "-c", "init.templateDir=", *args], cwd=self.root,
                                env=env, capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def put(self, name, text):
        (self.root / name).write_text(text, encoding="utf-8")

    def init_target(self):
        self.git("init", "--template=", "-b", "main")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.put("core.py", "def value(n):\n    return n\n")
        self.put("consumer.py", "def consume(n):\n    return n\n")
        self.put("check.py", "from consumer import consume\nassert consume(2) == 2\n")
        self.git("add", "core.py", "consumer.py", "check.py")
        self.git("commit", "-m", "baseline")
        self.put("protected.txt", "unrelated dirty work\n")
        (self.root / "protected-link").symlink_to("protected.txt")
        self.protected = self.sentinel()
        return self.git("rev-parse", "HEAD")

    def sentinel(self):
        return ((self.root / "protected.txt").read_bytes(),
                os.readlink(self.root / "protected-link"),
                (self.root / "protected-link").lstat().st_mode,
                self.git("ls-files", "--stage", "--", "protected.txt", "protected-link"))

    def check(self, expected=0):
        p = subprocess.run([sys.executable, "-B", "check.py"], cwd=self.root,
                           capture_output=True, text=True, timeout=5)
        self.assertEqual(p.returncode, expected, p.stderr)
        print(f"{self._testMethodName}: cross-ticket check exit={p.returncode}")
        return p

    def test_parent_and_native_prerequisite_evidence(self):
        candidates = {key for key, role in self.roles.items() if role == "work"}
        self.assertEqual(candidates, set("ABCD"))
        self.assertNotIn("P", candidates)
        a = {"closed": True, "local_pass": True, "integrated": False, "accepted": False}
        # Authored eligibility assessment: C waits despite closure/local pass.
        self.assertEqual(self.graph["blocked_by"]["C"], ["A"])
        self.assertFalse(a["integrated"] and a["accepted"])
        a["integrated"] = True
        self.assertFalse(a["integrated"] and a["accepted"])
        a["accepted"] = True  # Explicit synthetic acceptance, not user/agent acceptance.
        self.assertTrue(a["integrated"] and a["accepted"])
        self.assertEqual(self.original_graph, json.dumps(self.graph, sort_keys=True))

    def test_independent_and_shared_interface_ownership(self):
        self.assertTrue(self.owned["A"] & self.owned["B"])
        self.assertFalse(self.owned["A"] & self.owned["D"])
        assignments = ["A", "D"]  # B serialized; C waits for A accepted integration.
        self.assertNotIn("B", assignments)
        self.assertNotIn("C", assignments)
        # Different files can still share an unstable interface.
        interface_users = {"A": {"value-contract"}, "C": {"value-contract"}}
        self.assertTrue(interface_users["A"] & interface_users["C"])

    def test_one_unavailable_slot_and_no_recursive_pool(self):
        self.ledger["active"] = [{"id": "busy", "status": "idle-unfinished"}]
        ceiling = 2  # Fixture input matching the discovered shared contract.
        self.assertEqual(ceiling - len(self.ledger["active"]), 1)
        for axis in ("Standards", "Spec"):
            self.ledger["active"].append({"id": axis, "status": "read-only"})
            self.assertEqual(len(self.ledger["active"]), ceiling)
            self.ledger["active"].pop()  # Explicit synthetic completed return.
        self.assertEqual(self.ledger["active"][0]["id"], "busy")
        self.assertNotIn("nested_pool", self.ledger)

    def test_failed_uncertain_owner_retains_scope(self):
        self.init_target()
        self.put("core.py", "def value(n):\n    return n * 2\n")
        owner = {"id": "A", "state": "expired-unknown", "stopped_or_isolated": False}
        self.ledger["active"] = [owner]
        artifact = (self.root / "core.py").read_bytes()
        self.assertFalse(owner["stopped_or_isolated"])  # No replacement while unknown.
        self.assertEqual(len(self.ledger["active"]), 1)
        owner.update(state="stopped-confirmed", stopped_or_isolated=True)
        self.assertTrue(owner["stopped_or_isolated"])
        self.assertEqual(artifact, (self.root / "core.py").read_bytes())
        self.assertEqual(self.protected, self.sentinel())

    def test_uncertain_integration_is_inspected_not_replayed(self):
        base = self.init_target()
        self.git("switch", "-c", "ticket-a")
        self.put("core.py", "def value(n):\n    return n * 2\n")
        self.git("add", "core.py")
        self.git("commit", "-m", "A artifact")
        source = self.git("rev-parse", "HEAD")
        self.git("switch", "main")
        self.git("merge", "--ff-only", "ticket-a")  # Effect happened; pretend return lost.
        observed = self.git("rev-parse", "HEAD")
        self.assertNotEqual(base, observed)
        self.assertEqual(source, observed)
        self.git("merge-base", "--is-ancestor", source, "main")
        self.assertEqual(self.git("show", "main:core.py"), "def value(n):\n    return n * 2")
        before = self.git("rev-list", "--count", "main")
        # No repeated integration operation: only observed state is retained.
        self.assertEqual(before, self.git("rev-list", "--count", "main"))
        self.assertEqual(self.protected, self.sentinel())

    def test_resume_preserves_exhausted_lineage_and_unknown_usage(self):
        self.init_target()
        self.put("ledger.json", json.dumps(self.ledger, sort_keys=True))
        retained = json.loads((self.root / "ledger.json").read_text())
        self.assertEqual(retained, self.ledger)
        finding = retained["checkpoints"]["local-A"]
        self.assertEqual(finding["spent"], 2)
        # Moving the same cause into aggregate reporting cannot create a new allowance.
        report = {"aggregate_finding": finding, "root": retained["run"]}
        self.assertEqual(report["aggregate_finding"]["spent"], 2)
        self.assertTrue(retained["model"]["unknown_charge"])
        self.assertEqual(retained["model"]["attempted"], 1)
        self.assertEqual(self.protected, self.sentinel())

    def test_serial_integration_refreshes_cross_ticket_evidence(self):
        base = self.init_target()
        self.check()
        old = fingerprint(self.root)
        self.git("switch", "-c", "ticket-a")
        self.put("core.py", "def value(n):\n    return n * 2\n")
        self.git("add", "core.py")
        self.git("commit", "-m", "A artifact")
        a = self.git("rev-parse", "HEAD")
        self.git("switch", "main")
        self.git("merge", "--ff-only", "ticket-a")
        self.assertNotEqual(old, fingerprint(self.root))  # Old evidence stale.
        self.check()
        after_a = fingerprint(self.root)
        self.git("switch", "-c", "ticket-c")
        self.put("consumer.py", "from core import value\ndef consume(n):\n    return value(n) + 1\n")
        self.put("check.py", "from consumer import consume\nassert consume(2) == 5\n")
        self.check()  # Local result is not yet integrated evidence.
        self.git("add", "consumer.py", "check.py")
        self.git("commit", "-m", "C artifact")
        c = self.git("rev-parse", "HEAD")
        self.git("switch", "main")
        self.git("merge", "--ff-only", "ticket-c")
        self.assertNotEqual(after_a, fingerprint(self.root))
        self.git("merge-base", "--is-ancestor", a, "main")
        self.git("merge-base", "--is-ancestor", c, "main")
        self.check()
        pinned = fingerprint(self.root)
        self.put("core.py", "def value(n):\n    return n\n")
        failure = self.check(expected=1)
        self.assertIn("AssertionError", failure.stderr)  # Actual cross-ticket sensitivity.
        self.git("restore", "--source=HEAD", "--", "core.py")  # Fixture-owned fault only.
        self.check()
        self.assertEqual(pinned, fingerprint(self.root))
        self.assertNotEqual(base, self.git("rev-parse", "HEAD"))
        self.assertEqual(self.protected, self.sentinel())
        self.git("show-ref", "--verify", "refs/heads/ticket-a")
        self.git("show-ref", "--verify", "refs/heads/ticket-c")

    def test_instruction_boundaries_and_missing_runtime(self):
        entry = (PACKAGE / "SKILL.md").read_text().lower()
        dispatch = (PACKAGE / "references/dispatch.md").read_text().lower()
        aggregate = (PACKAGE / "references/aggregate.md").read_text().lower()
        recovery = (PACKAGE / "references/recovery.md").read_text().lower()
        for clause in ("one overall technical lead", "read-only library", "inspect-only delegate",
                       "do not silently substitute", "from this root", "missing/stale",
                       "shared worker/repair/model limits"):
            self.assertIn(clause, entry)
        for clause in ("closure", "work-on", "root-ledger", "one inspected result at a time",
                       "blocks multi-ticket execution"):
            self.assertIn(clause, dispatch)
        self.assertIn("local ticket passes do not establish", entry)
        self.assertIn("relocating an unresolved local cause cannot reset", aggregate)
        self.assertIn("not the old launch list", recovery)
        self.assertIn("no implicit abort/reset/cleanup", recovery)
        self.assertNotIn("../work-on/", entry + dispatch + aggregate + recovery)
        print("instruction assertions: static only, not runtime-adherence proof")


if __name__ == "__main__":
    unittest.main(verbosity=2)
