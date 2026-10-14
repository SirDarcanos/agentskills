import unittest
from pricing import total
class Existing(unittest.TestCase):
    def test_zero_discount(self): self.assertEqual(total([40, 60], 0), 100)
    def test_empty(self): self.assertEqual(total([], 0), 0)
