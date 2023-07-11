#!/usr/bin/python3
"""
    This is a function that returns an object
    (Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """To convert json string to python object"""
    result = json.loads(my_str)
    return result
