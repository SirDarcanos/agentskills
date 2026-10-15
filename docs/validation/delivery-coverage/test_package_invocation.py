"""Current Work On invocation guards; disposable package copies, no delivery.

These sensitivity tests protect the structural checker, not agent compliance.
"""
from contextlib import redirect_stdout
import importlib.util
import io
from pathlib import Path
import shutil
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location(
    "package_checks", Path(__file__).with_name("check_packages.py"))
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


class WorkOnInvocation(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.package = Path(self.temp.name) / "non-sibling-catalog-entry"
        shutil.copytree(REPO / "workflow/work-on", self.package, symlinks=True)
        self.entry = self.package / "SKILL.md"
        self.notice = (REPO / "LICENSE").read_bytes()

    def check(self):
        with redirect_stdout(io.StringIO()):
            checks.check_package(self.package, "work-on", checks.PACKAGES["work-on"], self.notice)

    def reject_change(self, old, new):
        text = self.entry.read_text()
        self.assertEqual(text.count(old), 1)
        self.entry.write_text(text.replace(old, new, 1))
        with self.assertRaises(AssertionError):
            self.check()

    def test_current_explicit_delivery_and_authorized_handoff_pass(self):
        self.assertFalse(checks.PACKAGES["work-on"])
        self.check()

    def test_command_only_metadata_regression_rejected(self):
        self.reject_change("name: work-on\n", "name: work-on\ndisable-model-invocation: true\n")

    def test_unbounded_user_request_route_rejected(self):
        self.reject_change("explicit user delivery request", "any user request")

    def test_unbounded_assignment_route_rejected(self):
        self.reject_change("bounded authorized assignment", "any assignment")

    def test_investigation_only_fix_authority_regression_rejected(self):
        self.reject_change("investigation-only requests confer no fix authority",
                           "investigation-only requests confer fix authority")


if __name__ == "__main__":
    unittest.main()
