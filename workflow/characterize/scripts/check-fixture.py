#!/usr/bin/env python3
"""Offline synthetic legacy characterization; not an agent-adherence test."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


CONTRACT = {
    "source": "synthetic owner agreement, revision 1",
    "intended": "Shipping is 5 units for nonempty orders, 0 for empty orders.",
    "defect": "Negative item prices should contribute zero, not reduce subtotal.",
    "unknown": "Receipt token format and audit flag intent are unspecified.",
}
LEGACY = '''import json
import sys
import uuid
prices = json.loads(sys.argv[1])
print(json.dumps({"shipping": 5 if prices else 0,
                  "subtotal": sum(prices),
                  "receipt": str(uuid.uuid4()),
                  "audit": True}))
'''


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(target, prices):
    result = subprocess.run(
        [sys.executable, str(target), json.dumps(prices)],
        capture_output=True, text=True, timeout=5, check=True,
    )
    return json.loads(result.stdout)


def protect_shipping(observation, prices):
    expected = 5 if prices else 0
    if observation["shipping"] != expected:
        raise AssertionError(
            "shipping invariant: expected %s, got %s"
            % (expected, observation["shipping"])
        )


class CharacterizationFixture(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="characterize-fixture-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.target = self.root / "legacy.py"
        self.target.write_text(LEGACY)
        self.original = digest(self.target)
        self.protected = self.root / "unrelated.txt"
        self.protected.write_text("Synthetic unrelated work: preserve exactly.\n")
        self.protected_digest = digest(self.protected)

    def tearDown(self):
        self.assertEqual(digest(self.target), self.original)
        self.assertEqual(digest(self.protected), self.protected_digest)

    def variant(self, name, old, new):
        self.assertEqual(LEGACY.count(old), 1)
        path = self.root / name
        path.write_text(LEGACY.replace(old, new))
        return path

    def test_intended_baseline(self):
        observations = []
        for prices in ([], [10], [10, -3]):
            actual = run(self.target, prices)
            protect_shipping(actual, prices)
            observations.append({"input": prices, "actual": actual})
        print(json.dumps({"baseline": observations, "contract": CONTRACT,
                          "source_sha256": self.original}, sort_keys=True))

    def test_defect_reproduction_is_not_acceptance(self):
        actual = run(self.target, [10, -3])
        self.assertEqual(actual["subtotal"], 7)  # Diagnostic only, not a gate.
        self.assertNotEqual(actual["subtotal"], 10)  # Intended outcome still fails.
        protect_shipping(actual, [10, -3])
        print("DEFECT diagnostic: subtotal 7, intended 10; excluded from protection gate.")

    def test_defect_correction_is_allowed_by_protection(self):
        corrected = self.variant("corrected.py", "sum(prices)",
                                 "sum(max(0, price) for price in prices)")
        actual = run(corrected, [10, -3])
        protect_shipping(actual, [10, -3])
        self.assertEqual(actual["subtotal"], 10)
        print("CORRECTION simulation: intended shipping protected; old defect not required.")

    def test_relevant_mutation_fails_then_original_passes(self):
        mutated = self.variant("mutated.py", "5 if prices else 0", "7 if prices else 0")
        with self.assertRaisesRegex(AssertionError, "shipping invariant: expected 5, got 7"):
            protect_shipping(run(mutated, [10]), [10])
        protect_shipping(run(self.target, [10]), [10])
        print("SENSITIVITY: isolated shipping mutation detected for intended reason; original green.")

    def test_nondeterminism_is_reported_not_snapshotted(self):
        observations = [run(self.target, [10]) for _ in range(3)]
        for actual in observations:
            protect_shipping(actual, [10])
        # Failure to observe variation is an honest inconclusive result, not retries.
        varied = len({row["receipt"] for row in observations}) > 1
        print(json.dumps({"repeats": 3, "raw": observations,
                          "variation": "observed" if varied else "inconclusive",
                          "comparison": "shipping only; receipt intent unknown",
                          "limit": "No token-format, ordering, concurrency or stability guarantee"},
                         sort_keys=True))
        self.assertTrue(all(row["audit"] is True for row in observations))
        print("UNKNOWN: audit True observed; no authority to make it desired acceptance.")


if __name__ == "__main__":
    print("Synthetic characterization: subprocess timeout 5s, at most 10 executions; no network.")
    unittest.main(verbosity=2)
