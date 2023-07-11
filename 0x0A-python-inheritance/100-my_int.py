#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """Myint class"""
    def __eq__(self, value):
        """function for equal =="""
        return super().__ne__(value)
    def __ne__(self, value):
        """function for not equal !="""
        return super().__eq__(value)
