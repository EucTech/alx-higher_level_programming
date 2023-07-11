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

    def to_json(self):
        """To return dicitonary repr of students"""
        return self.__dict__
