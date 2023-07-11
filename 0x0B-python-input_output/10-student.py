#!/usr/bin/python3
"""
    This is a  class Student that defines a student
"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of class attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """To return dicitonary repr of students"""
        if attrs is None:
            return self.__dict__
        else:
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
