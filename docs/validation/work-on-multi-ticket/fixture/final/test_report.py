import unittest
from report import render_names


class ReportTest(unittest.TestCase):
    def test_order_duplicates_and_empty_values(self):
        self.assertEqual(render_names([' A ', 'b', ' A ', '']), 'a, b, a, ')

    def test_empty_sequence(self):
        self.assertEqual(render_names([]), '')
