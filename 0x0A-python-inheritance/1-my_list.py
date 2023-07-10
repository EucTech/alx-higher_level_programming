#!/usr/bin/python3
""" a class MyList that inherits from list"""


class MyList(list):
    """mylist function"""
    def print_sorted(self):
        result = sorted(self)
        print(result)
