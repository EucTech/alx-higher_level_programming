#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """To test masinterger"""
    def test_max_intger(self):
        # Test case when the max number is at the begining
        my_lists = [21, 3, 5, 7, 6]
        self.assertEqual(max_integer(my_lists), 21)

        # Test case when the max number is in the middle
        my_lists = [21, 3, 55, 7, 6]
        self.assertEqual(max_integer(my_lists), 55)

        # Test case when the max number is at the end
        my_lists = [21, 3, 5, 7, 66]
        self.assertEqual(max_integer(my_lists), 66)

        # Test case when the lists contains negative numbers
        my_lists = [-21, -3, -5, -7, -6]
        self.assertEqual(max_integer(my_lists), -3)

        # Test case for when the list has one number
        my_lists = [7]
        self.assertEqual(max_integer(my_lists), 7)

        # Test when the list is empty
        my_lists = []
        self.assertIsNone(max_integer(my_lists))


if __name__ == '__main__':
    unittest.main()
