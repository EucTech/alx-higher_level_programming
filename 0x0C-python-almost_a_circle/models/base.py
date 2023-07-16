#!/usr/bin/python3
"""The BASE CLASS"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """To return json string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
