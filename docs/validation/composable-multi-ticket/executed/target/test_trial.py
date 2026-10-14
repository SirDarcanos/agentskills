import unittest
from render import render
from normalize import normalize
from pipeline import make_receipt

class A(unittest.TestCase):
    def test_render(self):
        self.assertEqual(render("Ada"), "Receipt: Ada")

class B(unittest.TestCase):
    def test_trim(self):
        self.assertEqual(normalize("  Ada  "), "Ada")
    def test_reject_blank(self):
        for value in ("", "   "):
            with self.assertRaises(ValueError):
                normalize(value)
    def test_reject_nonstring(self):
        for value in (None, 7):
            with self.assertRaises(ValueError):
                normalize(value)

class D(unittest.TestCase):
    def test_optional_upper(self):
        self.assertEqual(normalize(" Ada ", upper=True), "ADA")
        self.assertEqual(normalize(" Ada ", upper=False), "Ada")

class C(unittest.TestCase):
    def test_receipt(self):
        self.assertEqual(make_receipt(" Ada "), "Receipt: ADA")
    def test_invalid(self):
        for value in (" ", None):
            with self.assertRaises(ValueError):
                make_receipt(value)
