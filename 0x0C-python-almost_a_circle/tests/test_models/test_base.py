import os
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

        r = Rectangle(6, 8)
        d = Base.to_json_string([])
        res = '[]'
        self.assertEqual(d, res)

        r = Rectangle(6, 8)
        d = Base.to_json_string(None)
        res = '[]'
        self.assertEqual(d, res)

    def test_save_file_Empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_file_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_file_two(self):
        r1 = Rectangle(4, 5)
        Rectangle.save_to_file([r1])
        res = '[{"id": 1, "width": 4, "height": 5, "x": 0, "y": 0}]'
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), res)

    def test_save_file_3(self):
        r1 = Rectangle(4, 5, 6)
        Rectangle.save_to_file([r1])
        res = '[{"id": 1, "width": 4, "height": 5, "x": 6, "y": 0}]'
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), res)

    def test_save_file_two(self):
        r1 = Rectangle(4, 5, 6, 7)
        Rectangle.save_to_file([r1])
        res = '[{"id": 1, "width": 4, "height": 5, "x": 6, "y": 7}]'
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), res)

    def test_save_file_two(self):
        r1 = Rectangle(4, 5, 5, 7, 8)
        Rectangle.save_to_file([r1])
        res = '[{"id": 8, "width": 4, "height": 5, "x": 5, "y": 7}]'
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), res)

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        res = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        self.assertEqual(list_output, res)

    def test_from_json_string1(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        res = [
            {'id': 89, 'width': 10, 'height': 4}
        ]
        self.assertEqual(list_output, res)

    def test_from_json_string2(self):
        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        res = []
        self.assertEqual(list_output, res)

    def test_from_json_string4(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(None)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        res = '[Rectangle] (1) 1/0 - 3/5'
        self.assertEqual(r2.update(), res)

    def test_create_square(self):
        r1 = Square(3)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        res = '[Square] (1) 0/0 - 3'
        self.assertEqual(r2.update(), res)

    def test_load_from_file_Rec(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(4, 6)
        lput = [r1, r2]
        Rectangle.save_to_file(lput)
        oput = Rectangle.load_from_file()

        for x in range(len(lput)):
            self.assertEqual(lput[x].__str__(), oput[x].__str__())

    def test_load_from_file_Rec1(self):
        r1 = Rectangle(10, 7, 8)
        r2 = Rectangle(4, 6)
        lput = [r1, r2]
        Rectangle.save_to_file(lput)
        oput = Rectangle.load_from_file()

        for x in range(len(lput)):
            self.assertEqual(lput[x].__str__(), oput[x].__str__())

    def test_load_from_file_Rec2(self):
        r1 = Rectangle(10, 7)
        lput = [r1]
        Rectangle.save_to_file(lput)
        oput = Rectangle.load_from_file()

        for x in range(len(lput)):
            self.assertEqual(lput[x].__str__(), oput[x].__str__())

    def test_load_from_file_Rec3(self):
        r1 = Rectangle(10, 7, 2)
        lput = []
        Rectangle.save_to_file(lput)
        oput = Rectangle.load_from_file()

        for x in range(len(lput)):
            self.assertEqual(lput[x].__str__(), oput[x].__str__())

    def test_load_from_file_Rec4(self):
        oput = Rectangle.load_from_file()
        self.assertEqual(oput, [])

    def test_load_from_file_squ(self):
        r1 = Square(10, 7, 2, 8)
        r2 = Square(4, 6)
        lput = [r1, r2]
        Square.save_to_file(lput)
        oput = Square.load_from_file()

        for x in range(len(lput)):
            self.assertEqual(lput[x].__str__(), oput[x].__str__())

    def test_load_from_file_squ1(self):
        r1 = Square(10, 7, 2)
        lput = [r1]
        Square.save_to_file(lput)
        oput = Square.load_from_file()

        for x in range(len(lput)):
            self.assertEqual(lput[x].__str__(), oput[x].__str__())

    def test_load_from_file_squ2(self):
        r1 = Square(10)
        lput = [r1]
        Square.save_to_file(lput)
        oput = Square.load_from_file()

        for x in range(len(lput)):
            self.assertEqual(lput[x].__str__(), oput[x].__str__())

    def test_load_from_file_squ3(self):
        r1 = Square(10, 7)
        lput = []
        Square.save_to_file(lput)
        oput = Square.load_from_file()

        for x in range(len(lput)):
            self.assertEqual(lput[x].__str__(), [])

    def test_load_from_file_squ4(self):
        oput = Square.load_from_file()
        self.assertEqual(oput, [])
