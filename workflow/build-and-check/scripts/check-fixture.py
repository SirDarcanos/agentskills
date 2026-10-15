#!/usr/bin/env python3
"""Offline synthetic build/check exercises, not an agent-adherence test."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


CHECK = '''import json
from pathlib import Path
from convert import slug
assert slug("Hello World") == "hello-world"
assert slug("  Hello   World  ") == "hello-world"
config = json.loads(Path("config.json").read_text())
assert config["separator"] == "-"
text = Path("README.md").read_text()
assert "[Guide](guide.md)" in text
assert Path("guide.md").is_file()
print("existing behavior/config/link checks: PASS")
'''


class Fixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="build-check-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.put("convert.py", 'def slug(text):\n    return "-".join(text.lower().split())\n')
        self.put("check.py", CHECK)
        self.put("config.json", '{"separator": "-"}\n')
        self.put("README.md", '# Convert\n\n[Guide](guide.md)\n')
        self.put("guide.md", '# Guide\n')
        self.put("unrelated.txt", 'protected synthetic work\n')
        self.protected = self.digest("unrelated.txt")
        self.check_digest = self.digest("check.py")

    def put(self, name, text):
        (self.root / name).write_text(text, encoding="utf-8")

    def digest(self, name):
        return hashlib.sha256((self.root / name).read_bytes()).hexdigest()

    def check(self):
        result = subprocess.run(
            [sys.executable, "-B", "check.py"], cwd=self.root,
            capture_output=True, text=True, timeout=5,
        )
        print(f"check exit={result.returncode}: {(result.stdout or result.stderr).strip()}")
        return result

    def assert_preserved(self):
        self.assertEqual(self.protected, self.digest("unrelated.txt"))
        self.assertEqual(self.check_digest, self.digest("check.py"))

    def test_code_increment_reuses_existing_coverage(self):
        self.assertEqual(self.check().returncode, 0)
        self.put("convert.py", 'def slug(text):\n    words = text.lower().split()\n    return "-".join(words)\n')
        self.assertEqual(self.check().returncode, 0)
        self.assert_preserved()
        print("code increment: PASS; existing harness unchanged, zero new target tests")

    def test_documentation_and_configuration_increments(self):
        self.put("README.md", '# Convert\n\nConvert words to a lowercase slug.\n\n[Guide](guide.md)\n')
        self.assertEqual(self.check().returncode, 0)
        config = json.loads((self.root / "config.json").read_text())
        self.put("config.json", json.dumps(config, indent=2) + "\n")
        self.assertEqual(self.check().returncode, 0)
        self.assert_preserved()
        print("documentation then configuration: PASS; each checked before continuing")

    def test_failure_stops_dependent_increment_then_rechecks(self):
        original = (self.root / "convert.py").read_text()
        self.put("convert.py", 'def slug(text):\n    return text.lower().replace(" ", "-")\n')
        failed = self.check()
        self.assertNotEqual(failed.returncode, 0)
        self.assertIn("AssertionError", failed.stderr)
        self.assertNotIn("ModuleNotFoundError", failed.stderr)
        # This gate models caller behavior; it does not prove an agent obeys it.
        if failed.returncode == 0:
            self.put("dependent.txt", "should not run\n")
        self.assertFalse((self.root / "dependent.txt").exists())
        print("material behavior failure: BLOCKED; dependent artifact absent")
        self.put("convert.py", original)
        self.assertEqual(self.check().returncode, 0)
        self.put("dependent.txt", "resumed after current pass\n")
        self.assert_preserved()

    def test_unavailable_check_remains_unverified(self):
        result = {"status": "blocked", "reason": "synthetic consumer unavailable", "verified": False}
        self.assertFalse(result["verified"])
        self.assertFalse((self.root / "dependent.txt").exists())
        self.assert_preserved()
        print("unavailable material consumer: BLOCKED/unverified (reporting oracle only)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
