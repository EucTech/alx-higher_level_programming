import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test__init__(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        b = Base(5)
        self.assertEqual(b.id, 5)
        b = Base(None)
        self.assertEqual(b.id, 3)
        b = Base(6.7)
        self.assertEqual(b.id, 6.7)
        b = Base(-8)
        self.assertEqual(b.id, -8)
        b = Base("hello")
        self.assertEqual(b.id, 'hello')
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_to_json_string(self):
        r = Rectangle(10, 7, 2, 8)
        dic = r.to_dictionary()
        d = Base.to_json_string([dic])
        res = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(d, res)

        r = Rectangle(10, 2, 8)
        dic = r.to_dictionary()
        d = Base.to_json_string([dic])
        res = '[{"id": 2, "width": 10, "height": 2, "x": 8, "y": 0}]'
        self.assertEqual(d, res)

        r = Rectangle(10, 7)
        dic = r.to_dictionary()
        d = Base.to_json_string([dic])
        res = '[{"id": 3, "width": 10, "height": 7, "x": 0, "y": 0}]'
        self.assertEqual(d, res)

        r = Rectangle(12, 6, 7, 2, 8)
        dic = r.to_dictionary()
        d = Base.to_json_string([dic])
        res = '[{"id": 8, "width": 12, "height": 6, "x": 7, "y": 2}]'
        self.assertEqual(d, res)
