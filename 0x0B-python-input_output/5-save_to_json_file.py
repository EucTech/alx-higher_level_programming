#!/usr/bin/python3
"""
    This is a function that writes an Object
    to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to textfile with JSON"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
