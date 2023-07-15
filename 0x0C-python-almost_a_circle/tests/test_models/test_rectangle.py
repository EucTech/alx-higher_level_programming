import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        self.up = Rectangle(10, 10, 10, 10, 10)

    def test_integers(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 1)
        r = Rectangle(5, 6, 0, 9, None)
        self.assertEqual(r.id, 2)
        r1 = Rectangle(2, 10)
        self.assertEqual(r1.id, 3)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)
        r3 = Rectangle(2, 50, 0, 0, 333333)
        self.assertEqual(r3.id, 333333)
        re4 = Rectangle(2, 4, 0, 0, -4444444)
        self.assertEqual(re4.id, -4444444)
        re5 = Rectangle(10, 8, 0, 0, 0)
        self.assertEqual(re5.id, 0)
        rec = Rectangle(2, 3, 0, 0, 3.4)
        self.assertEqual(rec.id, 3.4)
        r1 = Rectangle(26, 10)
        self.assertEqual(r1.id, 4)

    def test_zero_x_y(self):
        r = Rectangle(7, 9)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        r = Rectangle(9, 8, 0, 7, 9)
        self.assertEqual(r.x, 0)
        r = Rectangle(6, 8, 6, 0, 7)
        self.assertEqual(r.y, 0)

    def test_positive_numbers(self):
        r = Rectangle(5, 8)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 8)
        r1 = Rectangle(4, 6, 9, 4, 9)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 9)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 9)

    def test_typeerror_string(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, "3")
        with self.assertRaises(TypeError):
            r1 = Rectangle("3", 10)
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 5, "4", 8, 12)
        with self.assertRaises(TypeError):
            r3 = Rectangle(2, 3, 5, "5", 8)
        with self.assertRaises(TypeError):
            r4 = Rectangle("4", "5", "9", "7", 3)

    def test_typeerror_float(self):
        with self.assertRaises(TypeError):
            r = Rectangle(4.0, 4)
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 4.0)
        with self.assertRaises(TypeError):
            r2 = Rectangle(4, 4, 9.0, 9, 3)
        with self.assertRaises(TypeError):
            r3 = Rectangle(4, 4, 5, 4.5, 2)
        with self.assertRaises(TypeError):
            r4 = Rectangle(4.0, 7.888, 8.9, 7, 0)

    def test_none_float_inf(self):
        with self.assertRaises(TypeError):
            r = Rectangle(float('inf'), 4)
        with self.assertRaises(TypeError):
            r1 = Rectangle(3, float('inf'))
        with self.assertRaises(TypeError):
            r2 = Rectangle(None, 4)
        with self.assertRaises(TypeError):
            r = Rectangle(9, None)
        with self.assertRaises(TypeError):
            r = Rectangle(5, 4, float('inf'), 4, 8)
        with self.assertRaises(TypeError):
            r = Rectangle(4, 4, 7, float('inf'), 9)
        with self.assertRaises(TypeError):
            r = Rectangle(4, 6, None, 6, 9)
        with self.assertRaises(TypeError):
            r = Rectangle(4, 4, 6, None, 8)

    def test_boolean(self):
        with self.assertRaises(TypeError):
            r = Rectangle(True, 4, 6, 5, 8)
        with self.assertRaises(TypeError):
            r = Rectangle(4, True, 6, 6, 8)
        with self.assertRaises(TypeError):
            r = Rectangle(4, 4, 6, True, 8)
        with self.assertRaises(TypeError):
            r = Rectangle(4, 4, True, 63, 8)

    def test_list(self):
        with self.assertRaises(TypeError):
            r = Rectangle(4, 4, [6, 7, 8], 63, 8)
        with self.assertRaises(TypeError):
            r = Rectangle([7, 8, 0, 9], 4, 6, 63, 8)
        with self.assertRaises(TypeError):
            r = Rectangle(4, [4, 6, 7], 9, 63, 8)
        with self.assertRaises(TypeError):
            r = Rectangle(4, 4, 3, [63, 8, 6], 8)

    def test_zero_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 9)
        with self.assertRaises(ValueError):
            r = Rectangle(9, 0)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-4, 9)
        with self.assertRaises(ValueError):
            r = Rectangle(7, -9)
        with self.assertRaises(ValueError):
            r = Rectangle(7, 9, -5)
        with self.assertRaises(ValueError):
            r = Rectangle(7, 9, 5, -9)
        with self.assertRaises(ValueError):
            r = Rectangle(-17, -29, -3, -9, 0)

    def test_area(self):
        """Checking for area of a rectangle"""
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)
        r1 = Rectangle(6, 2)
        self.assertEqual(r1.area(), 12)
        r2 = Rectangle(2, 10, 0, 0, 12)
        self.assertEqual(r2.area(), 20)

    def test_display(self):
        d = Rectangle(2, 6)
        res = '##\n' * 6
        with patch('sys.stdout', new=StringIO()) as pout:
            d.display()
            self.assertEqual(pout.getvalue(), res)

        d = Rectangle(6, 2)
        res = '######\n' * 2
        with patch('sys.stdout', new=StringIO()) as pout:
            d.display()
            self.assertEqual(pout.getvalue(), res)

        d = Rectangle(2, 2)
        res = '##\n' * 2
        with patch('sys.stdout', new=StringIO()) as pout:
            d.display()
            self.assertEqual(pout.getvalue(), res)

        d = Rectangle(3, 4, 0, 0, 6)
        res = '###\n###\n###\n###\n'
        with patch('sys.stdout', new=StringIO()) as pout:
            d.display()
            self.assertEqual(pout.getvalue(), res)

        d = Rectangle(3, 4, 2, 2, 6)
        res = '\n\n  ###\n  ###\n  ###\n  ###\n'
        with patch('sys.stdout', new=StringIO()) as pout:
            d.display()
            self.assertEqual(pout.getvalue(), res)

        d = Rectangle(3, 4, 5, 2, 6)
        res = '\n\n     ###\n     ###\n     ###\n     ###\n'
        with patch('sys.stdout', new=StringIO()) as pout:
            d.display()
            self.assertEqual(pout.getvalue(), res)

    def test__str(self):
        d = Rectangle(4, 6, 2, 1, 12)
        res = '[Rectangle] (12) 2/1 - 4/6'
        self.assertEqual(d.__str__(), res)

        d = Rectangle(4, 6, 0, 0, 12)
        res = '[Rectangle] (12) 0/0 - 4/6'
        self.assertEqual(d.__str__(), res)

        d = Rectangle(6, 4, 2, 1, None)
        res = '[Rectangle] (1) 2/1 - 6/4'
        self.assertEqual(d.__str__(), res)

        d = Rectangle(6, 4, 2, 1, 0)
        res = '[Rectangle] (0) 2/1 - 6/4'
        self.assertEqual(d.__str__(), res)

        d = Rectangle(6, 4, 0, 2, 6)
        res = '[Rectangle] (6) 0/2 - 6/4'
        self.assertEqual(d.__str__(), res)

        d = Rectangle(6, 4, 2)
        res = '[Rectangle] (2) 2/0 - 6/4'
        self.assertEqual(d.__str__(), res)

    def test_args_update(self):
        self.up.update(2)
        res = "[Rectangle] (2) 10/10 - 10/10"
        self.assertEqual(self.up.update(), res)

        self.up.update(2, 5)
        res = "[Rectangle] (2) 10/10 - 5/10"
        self.assertEqual(self.up.update(), res)

        self.up.update(2, 5, 8)
        res = "[Rectangle] (2) 10/10 - 5/8"
        self.assertEqual(self.up.update(), res)

        self.up.update(2, 5, 8, 7)
        res = "[Rectangle] (2) 7/10 - 5/8"
        self.assertEqual(self.up.update(), res)

        self.up.update(2, 5, 8, 7, 9)
        res = "[Rectangle] (2) 7/9 - 5/8"
        self.assertEqual(self.up.update(), res)

    def test_kwargs_updates(self):
        k = Rectangle(10, 10, 10, 10)
        k.update(height=2)
        res = "[Rectangle] (1) 10/10 - 10/2"
        self.assertEqual(k.update(), res)

        k.update(width=2, x=2)
        res = "[Rectangle] (1) 2/10 - 2/2"
        self.assertEqual(k.update(), res)

        k.update(y=3, width=4, x=5, id=45)
        res = "[Rectangle] (45) 5/3 - 4/2"
        self.assertEqual(k.update(), res)

        k.update(x=4, height=44, width=2, y=2)
        res = "[Rectangle] (45) 4/2 - 2/44"
        self.assertEqual(k.update(), res)

        k.update(width=2, height=9, y=7, x=3, id=66)
        res = "[Rectangle] (66) 3/7 - 2/9"
        self.assertEqual(k.update(), res)
