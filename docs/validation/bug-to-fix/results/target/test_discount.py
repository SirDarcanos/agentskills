import unittest
from pricing import total
class Discount(unittest.TestCase):
    def test_fraction(self): self.assertEqual(total([40, 60], .1), 90)
    def test_empty_fraction(self): self.assertEqual(total([], .1), 0)
