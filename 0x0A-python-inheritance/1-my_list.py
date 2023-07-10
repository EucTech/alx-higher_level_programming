#!/usr/python3
""" a class MyList that inherits from list"""

class MyList(list):
    def print_sorted(self):
        result = sorted(self)
        print(result)
