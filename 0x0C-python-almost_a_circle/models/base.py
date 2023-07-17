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

    @classmethod
    def save_to_file(cls, list_objs):
        """
            To write JSON string representaion of
            list_objs to file
        """
        filename = cls.__name__ + ".json"
        llist = []
        if list_objs is None:
            with open(filename, 'w') as f:
                f.write("[]")
        elif list_objs is not None:
            for obj in range(len(list_objs)):
                llist.append(list_objs[obj].to_dictionary())

            j_list = cls.to_json_string(llist)
            with open(filename, 'w', encoding="utf-8") as f:
                f.write(j_list)

    @staticmethod
    def from_json_string(json_string):
        """
            that returns the list of the JSON string
            representation json_string
        """
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)
