#!/usr/python3
""" a class MyList that inherits from list"""

class MyList:
    def __init__(self, lists=[]):
        self.lists = lists
    
    def append(self, value):
        if isinstance(value, int):
            self.lists.append(value)
        else:
            raise ValueError("lists must integer")

    def print_sorted(self):
        result = sorted(self.lists)
        print(result)

    def __str__(self):
        return str(self.lists)
