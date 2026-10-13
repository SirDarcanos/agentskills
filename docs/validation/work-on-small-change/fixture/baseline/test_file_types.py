import unittest

from file_types import is_markdown, markdown_files


class FileTypesTests(unittest.TestCase):
    def test_lowercase_markdown(self):
        self.assertTrue(is_markdown("notes.md"))

    def test_non_markdown_and_final_suffix(self):
        for name in ("", "notes", "notes.txt", "notes.markdown", "notes.md.bak"):
            with self.subTest(name=name):
                self.assertFalse(is_markdown(name))

    def test_no_whitespace_trimming(self):
        self.assertFalse(is_markdown("notes.md "))

    def test_filter_preserves_order_and_duplicates(self):
        names = ["b.md", "a.txt", "a.md", "b.md"]
        self.assertEqual(markdown_files(names), ["b.md", "a.md", "b.md"])


if __name__ == "__main__":
    unittest.main()
