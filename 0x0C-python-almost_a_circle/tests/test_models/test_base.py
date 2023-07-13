import unittest
from models.base import Base


class TestBase(unittest.TestCase):

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
