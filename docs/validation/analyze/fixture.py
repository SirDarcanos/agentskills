"""Synthetic sources for direct analysis walkthroughs; not product implementation."""
import unittest


def export_rows(rows, allowed):
    if not allowed:
        raise PermissionError("export denied")
    return "\n".join(str(row) for row in rows)


def download(rows, allowed):
    return {"content_type": "text/plain", "body": export_rows(rows, allowed)}


def legacy_label(value):
    return str(value).strip().upper()


HELP_HEADING = "Records"


class Baseline(unittest.TestCase):
    def test_export(self):
        self.assertEqual(export_rows([1, 2], True), "1\n2")
        self.assertEqual(export_rows([], True), "")

    def test_denial(self):
        with self.assertRaises(PermissionError):
            download([1], False)

    def test_download(self):
        self.assertEqual(download([1], True), {"content_type": "text/plain", "body": "1"})

    def test_legacy(self):
        self.assertEqual(legacy_label(" a "), "A")


if __name__ == "__main__":
    unittest.main(verbosity=2)
