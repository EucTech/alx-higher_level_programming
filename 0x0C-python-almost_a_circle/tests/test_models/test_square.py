import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_str_one_parameter(self):
        s = Square(3)
        res = "[Square] (1) 0/0 - 3"
        self.assertEqual(s.__str__(), res)

    def test_square_str_two_parameter(self):
        s = Square(3, 5)
        res = "[Square] (1) 5/0 - 3"
        self.assertEqual(s.__str__(), res)

    def test_square_str_three_parameter(self):
        s = Square(4, 6, 7, 5)
        res = "[Square] (5) 6/7 - 4"
        self.assertEqual(s.__str__(), res)

    def test_square_area(self):
        s = Square(2, 2)
        res = 4
        self.assertEqual(s.area(), res)

    def test_square_area_two_value(self):
        s = Square(4, 4)
        res = 16
        self.assertEqual(s.area(), res)

    def test_square_display_size(self):
        s = Square(3)
        res = "###\n" * 3
        with patch('sys.stdout', new=StringIO()) as pout:
            s.display()
            self.assertEqual(pout.getvalue(), res)

    def test_square_display_size_x(self):
        s = Square(3, 2)
        res = '  ###\n  ###\n  ###\n' 
        with patch('sys.stdout', new=StringIO()) as pout:
            s.display()
            self.assertEqual(pout.getvalue(), res)

    def test_square_display_size_x_y(self):
        s = Square(3, 2, 3)
        res = '\n\n\n  ###\n  ###\n  ###\n'
        with patch('sys.stdout', new=StringIO()) as pout:
            s.display()
            self.assertEqual(pout.getvalue(), res)

    def test_square_display_size_x_y_id(self):
        s = Square(4, 4, 2, 5)
        res = '\n\n    ####\n    ####\n    ####\n    ####\n'
        with patch('sys.stdout', new=StringIO()) as pout:
            s.display()
            self.assertEqual(pout.getvalue(), res)

    def test_typeerror_string(self):
        with self.assertRaises(TypeError):
            r = Square(10, "3")
        with self.assertRaises(TypeError):
            r1 = Square("3", 10)
        with self.assertRaises(TypeError):
            r2 = Square(10, "4", 8, 12)
        with self.assertRaises(TypeError):
            r3 = Square(2, 5, "5", 8)
        with self.assertRaises(TypeError):
            r4 = Square("4", "5", "7", 3)

    def test_typeerror_float(self):
        with self.assertRaises(TypeError):
            r = Square(4.0, 4)
        with self.assertRaises(TypeError):
            r1 = Square(4, 4.0)
        with self.assertRaises(TypeError):
            r2 = Square(4, 9.0, 9, 3)
        with self.assertRaises(TypeError):
            r3 = Square(4, 5, 4.5, 2)
        with self.assertRaises(TypeError):
            r4 = Square(4.0, 7.888, 8.9, 7)

    def test_none_float_inf(self):
        with self.assertRaises(TypeError):
            r = Square(float('inf'), 4)
        with self.assertRaises(TypeError):
            r1 = Square(3, float('inf'))
        with self.assertRaises(TypeError):
            r2 = Square(None, 4)
        with self.assertRaises(TypeError):
            r = Square(9, None)
        with self.assertRaises(TypeError):
            r = Square(5, 4, float('inf'), 4)
        with self.assertRaises(TypeError):
            r = Square(4, 4, float('inf'), 9)
        with self.assertRaises(TypeError):
            r = Square(4, 6, None, 9)
        with self.assertRaises(TypeError):
            r = Square(4, None, 9, 8)

    def test_boolean(self):
        with self.assertRaises(TypeError):
            r = Square(True, 4, 6, 5)
        with self.assertRaises(TypeError):
            r = Square(4, True, 6, 8)
        with self.assertRaises(TypeError):
            r = Square(4, 4, True, 8)

    def test_list(self):
        with self.assertRaises(TypeError):
            r = Square(4, 4, [6, 7, 8], 63)
        with self.assertRaises(TypeError):
            r = Square([7, 8, 0, 9], 6, 63, 8)
        with self.assertRaises(TypeError):
            r = Square(4, [4, 6, 7], 9, 63, 8)
        with self.assertRaises(TypeError):
            r = Square(4, 4, [63, 8, 6], 8)

    def test_zero_value(self):
        with self.assertRaises(ValueError):
            r = Square(0)
        with self.assertRaises(ValueError):
            r = Square(0, 6)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            r = Square(-4, 9)
        with self.assertRaises(ValueError):
            r = Square(7, -9)
        with self.assertRaises(ValueError):
            r = Square(7, 9, -5)
        with self.assertRaises(ValueError):
            r = Square(-17, -29, -9, 0)

    def test_args_update(self):
        up = Square(10, 10, 10)
        up.update(2)
        res = "[Square] (2) 10/10 - 10"
        self.assertEqual(up.update(), res)

        up.update(2, 5)
        res = "[Square] (2) 10/10 - 5"
        self.assertEqual(up.update(), res)

        up.update(4, 5, 8)
        res = "[Square] (4) 8/10 - 5"
        self.assertEqual(up.update(), res)

        up.update(6, 5, 8, 7)
        res = "[Square] (6) 8/7 - 5"
        self.assertEqual(up.update(), res)

    def test_kwargs_updates(self):
        k = Square(10, 10, 10)
        k.update(size=2)
        res = "[Square] (1) 10/10 - 2"
        self.assertEqual(k.update(), res)

        k.update(size=2, x=2)
        res = "[Square] (1) 2/10 - 2"
        self.assertEqual(k.update(), res)

        k.update(y=3, size=4, x=5, id=45)
        res = "[Square] (45) 5/3 - 4"
        self.assertEqual(k.update(), res)

        k.update(x=4, size=44, y=2)
        res = "[Square] (45) 4/2 - 44"
        self.assertEqual(k.update(), res)

        k.update(size=2, y=7, x=3, id=66)
        res = "[Square] (66) 3/7 - 2"
        self.assertEqual(k.update(), res)
