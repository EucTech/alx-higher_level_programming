#!/usr/bin/python3
"""The BASE CLASS"""


class Base:
    """Base"""
    __nb_objects = 0
    def __init__(self, id=None):
        """instantiation"""
        if id is not None:
           self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
