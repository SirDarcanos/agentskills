#!/usr/bin/env python3
"""Offline synthetic TDD evidence, not an agent/runtime acceptance test."""

import subprocess
import sys
import tempfile
from pathlib import Path


RED = '''def checkout_total(prices):
    return sum(prices)
'''
GREEN = '''def checkout_total(prices):
    if sum(prices) >= 50:
        return sum(prices)
    return sum(prices) + 5
'''
REFACTORED = '''def checkout_total(prices):
    subtotal = sum(price for price in prices)
    shipping = 0 if subtotal >= 50 else 5
    return subtotal + shipping
'''
EXISTING = '''import unittest
from checkout import checkout_total

class CheckoutTests(unittest.TestCase):
    def test_qualifying_cart_has_free_shipping(self):
        self.assertEqual(checkout_total([20, 30]), 50)
'''
INCREMENT = '''
    def test_small_cart_includes_shipping(self):
        self.assertEqual(checkout_total([10, 20]), 35)
'''
TAUTOLOGY = '''import unittest
from checkout import checkout_total

class RejectedOracle(unittest.TestCase):
    def test_result_matches_itself(self):
        self.assertEqual(checkout_total([10, 20]), checkout_total([10, 20]))
'''
COUPLED = '''import inspect
import unittest
from checkout import checkout_total

class RejectedCoupling(unittest.TestCase):
    def test_internal_expression(self):
        self.assertIn("sum(prices)", inspect.getsource(checkout_total))
'''


def run(root, label, filename, expected_exit, expected_output):
    result = subprocess.run(
        [sys.executable, "-B", "-m", "unittest", "-v", filename],
        cwd=root, text=True, capture_output=True, timeout=20,
    )
    output = result.stdout + result.stderr
    print(f"\n{label}: exit {result.returncode}\n{output}", flush=True)
    if result.returncode != expected_exit or expected_output not in output:
        raise AssertionError(f"{label}: unexpected result")


def main():
    with tempfile.TemporaryDirectory(prefix="tdd-fixture-") as directory:
        root = Path(directory)
        code = root / "checkout.py"
        checks = root / "test_checkout.py"
        code.write_text(RED)
        checks.write_text(EXISTING)
        run(root, "Existing coverage baseline", "test_checkout", 0, "Ran 1 test")
        (root / "test_tautology.py").write_text(TAUTOLOGY)
        run(root, "Rejected oracle passes despite missing shipping", "test_tautology", 0, "OK")
        checks.write_text(EXISTING + INCREMENT)
        behavioral_tests = checks.read_bytes()
        run(root, "Meaningful red; existing coverage retained", "test_checkout", 1, "30 != 35")
        code.write_text(GREEN)
        run(root, "Minimal green", "test_checkout", 0, "Ran 2 tests")
        (root / "test_coupling.py").write_text(COUPLED)
        run(root, "Coupled probe before refactor", "test_coupling", 0, "OK")
        code.write_text(REFACTORED)
        run(root, "Behavior-preserving refactor", "test_checkout", 0, "Ran 2 tests")
        run(root, "Rejected coupling breaks on equivalent behavior", "test_coupling", 1, "not found in")
        if checks.read_bytes() != behavioral_tests:
            raise AssertionError("Behavioral expectations changed during refactor")
        # Diagnostic anti-examples are removed, not promoted to retained coverage.
        (root / "test_tautology.py").unlink()
        (root / "test_coupling.py").unlink()
        run(root, "Final retained suite", "test_checkout", 0, "Ran 2 tests")
    print("PASS: red–green–refactor, coverage reuse, and two rejected anti-examples")


if __name__ == "__main__":
    main()
