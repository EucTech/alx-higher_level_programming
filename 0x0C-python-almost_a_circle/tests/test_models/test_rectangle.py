import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_positive_integers(self):
        r =  Rectangle(10, 2)
        self.assertEqual(r.id, 1)
        r = Rectangle(5, 6, 0, 9, None)
        self.assertEqual(r.id, 2)
        r1 = Rectangle(2, 10)
        self.assertEqual(r1.id, 3)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)
        r3 = Rectangle(2, 50, 0, 0, 333333)
        self.assertEqual(r3.id, 333333)

    def test_Empty_and_negative_integer(self):
        re3 = Rectangle(-10, -3, 0, 0, -12)
        self.assertEqual(re3.id, -12)
        re4 = Rectangle(-2, -4, 0, 0, -4444444)
        self.assertEqual(re4.id, -4444444)
        re5 = Rectangle(10, 8, 0, 0, 0)
        self.assertEqual(re5.id, 0)

    def test_float_string(self):
        rec = Rectangle(2, 3, 0, 0, 3.4)
        self.assertEqual(rec.id, 3.4)
