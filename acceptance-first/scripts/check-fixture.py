#!/usr/bin/env python3
"""Offline synthetic workflow; standard library only, no user-project writes."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

# Synthetic owner agreement, not inferred from implementation.
AGREEMENT = {
    "revision": "synthetic-v1",
    "AC1": "Submitting an order returns a receipt and persists that order.",
    "AC2": "A nonpositive quantity is rejected without persisting an order.",
    "AC3": None,  # Owner has not decided whether duplicate requests are accepted.
    "AC4": "A real remote payment gateway confirms payment.",
}
STORE = '''import sqlite3

def save(path, quantity):
    with sqlite3.connect(path) as db:
        db.execute("CREATE TABLE IF NOT EXISTS orders (quantity INTEGER)")
        db.execute("INSERT INTO orders VALUES (?)", (quantity,))
'''
BASE = '''from store import save

def submit(path, quantity):
    return {"status": "pending"}
'''
SLICE = '''from store import save

def submit(path, quantity):
    save(path, quantity)
    return {"status": "accepted", "quantity": quantity}
'''
FINAL = '''from store import save

def submit(path, quantity):
    if quantity <= 0:
        return {"status": "rejected"}
    save(path, quantity)
    return {"status": "accepted", "quantity": quantity}
'''
RUNNER = '''import json, sqlite3, sys
from api import submit
receipt = submit(sys.argv[1], int(sys.argv[2]))
with sqlite3.connect(sys.argv[1]) as db:
    exists = db.execute("SELECT name FROM sqlite_master WHERE name='orders'").fetchone()
    rows = db.execute("SELECT quantity FROM orders").fetchall() if exists else []
print(json.dumps({"receipt": receipt, "rows": rows}))
'''


def disposition(criterion, material_available=True):
    """Synthetic reporting oracle, not enforcement of agent behavior."""
    if AGREEMENT[criterion] is None:
        return {"criterion": criterion, "state": "blocked", "verified": False,
                "reason": "owner decision required"}
    if not material_available:
        return {"criterion": criterion, "state": "unverified", "verified": False,
                "reason": "material remote gateway unavailable; no substitute pass"}
    return {"criterion": criterion, "state": "ready", "verified": False}


class AcceptanceFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="acceptance-first-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name, body in {"api.py": BASE, "store.py": STORE,
                           "runner.py": RUNNER, "protected.txt": "unrelated\n",
                           "agreement.json": json.dumps(AGREEMENT, sort_keys=True)}.items():
            (self.root / name).write_text(body)
        self.protected = {name: self.digest(name) for name in
                          ("protected.txt", "agreement.json", "store.py", "runner.py")}

    def digest(self, name):
        return hashlib.sha256((self.root / name).read_bytes()).hexdigest()

    def tearDown(self):
        for name, digest in self.protected.items():
            self.assertEqual(self.digest(name), digest, name)

    def observe(self, quantity):
        # Each invocation has a fresh real SQLite database, not a mocked store.
        database = self.root / ("case-" + str(len(list(self.root.glob('case-*')))) + ".db")
        result = subprocess.run(
            [sys.executable, "-B", "runner.py", str(database), str(quantity)],
            cwd=self.root, capture_output=True, text=True, timeout=5)
        self.assertEqual(result.returncode, 0, result.stderr)
        observed = json.loads(result.stdout)
        print(json.dumps({"quantity": quantity, "observed": observed}), flush=True)
        return observed

    def accepted(self):
        actual = self.observe(2)
        self.assertEqual(actual["receipt"], {"status": "accepted", "quantity": 2},
                         "AC1 receipt mismatch")
        self.assertEqual(actual["rows"], [[2]], "AC1 order not persisted")

    def rejected(self, quantity):
        actual = self.observe(quantity)
        self.assertEqual(actual["receipt"], {"status": "rejected"}, "AC2 rejection missing")
        self.assertEqual(actual["rows"], [], "AC2 rejection persisted an order")

    def test_workflow_red_two_increments_green(self):
        with self.assertRaisesRegex(AssertionError, "AC1 receipt mismatch"):
            self.accepted()
        print("AC1 meaningful red: runnable workflow returns pending, not receipt", flush=True)
        (self.root / "api.py").write_text(SLICE)
        self.accepted()
        with self.assertRaisesRegex(AssertionError, "AC2 rejection missing"):
            self.rejected(0)
        print("AC2 meaningful red: nonpositive quantity accepted", flush=True)
        (self.root / "api.py").write_text(FINAL)
        self.accepted()
        self.rejected(0)
        self.rejected(-1)
        print("AC1/AC2 verified: API -> workflow -> SQLite; acceptance unchanged", flush=True)

    def test_cross_component_persistence_regression(self):
        (self.root / "api.py").write_text(FINAL.replace("    save(path, quantity)\n", ""))
        with self.assertRaisesRegex(AssertionError, "AC1 order not persisted"):
            self.accepted()
        (self.root / "api.py").write_text(FINAL)
        self.accepted()

    def test_rejection_side_effect_regression(self):
        (self.root / "api.py").write_text(FINAL.replace(
            "        return {\"status\": \"rejected\"}",
            "        save(path, quantity)\n        return {\"status\": \"rejected\"}"))
        with self.assertRaisesRegex(AssertionError, "AC2 rejection persisted an order"):
            self.rejected(0)
        (self.root / "api.py").write_text(FINAL)
        self.rejected(0)

    def test_ambiguous_commitment_blocks_without_edit(self):
        before = self.digest("api.py")
        result = disposition("AC3")
        self.assertEqual(result["state"], "blocked")
        self.assertFalse(result["verified"])
        self.assertEqual(self.digest("api.py"), before)
        print(json.dumps(result), flush=True)

    def test_unavailable_material_boundary_never_passes(self):
        result = disposition("AC4", material_available=False)
        self.assertEqual(result["state"], "unverified")
        self.assertFalse(result["verified"])
        print(json.dumps(result), flush=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
