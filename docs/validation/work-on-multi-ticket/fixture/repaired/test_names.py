import unittest
from names import normalize_name


class NamesTest(unittest.TestCase):
    def test_existing_lowercase(self):
        self.assertEqual(normalize_name('a'), 'a')

    def test_normalization(self):
        self.assertEqual(normalize_name(' A '), 'a')
        self.assertEqual(normalize_name(''), '')
        self.assertEqual(normalize_name(' \t '), '')
