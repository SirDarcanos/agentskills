import unittest
from names import normalize_name


class NamesTest(unittest.TestCase):
    def test_existing_lowercase(self):
        self.assertEqual(normalize_name('a'), 'a')
