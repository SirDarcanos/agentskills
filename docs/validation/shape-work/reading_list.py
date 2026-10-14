"""Synthetic analysis source, not a product implementation or skill runtime.

Python 3.9+. Baseline checks only; the requested pinning feature stays unbuilt.
"""
import unittest


def visible_books(books, reader):
    """Current list preserves input order and hides other readers' entries."""
    return [book["title"] for book in books if book["reader"] == reader]


def reading_page(books, reader):
    return {"heading": "My reading list", "titles": visible_books(books, reader)}


class Baseline(unittest.TestCase):
    def setUp(self):
        self.books = [
            {"reader": "A", "title": "Second title"},
            {"reader": "B", "title": "Private title"},
            {"reader": "A", "title": "First title"},
        ]

    def test_input_order(self):
        self.assertEqual(visible_books(self.books, "A"), ["Second title", "First title"])

    def test_privacy(self):
        self.assertNotIn("Private title", reading_page(self.books, "A")["titles"])

    def test_empty(self):
        self.assertEqual(reading_page([], "A"), {"heading": "My reading list", "titles": []})


if __name__ == "__main__":
    unittest.main(verbosity=2)
