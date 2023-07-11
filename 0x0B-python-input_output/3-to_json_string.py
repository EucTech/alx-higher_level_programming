#!/usr/bin/python3
"""
    This is function that returns the JSON
    representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """convert python object to JSON string"""
    result = json.dumps(my_obj)
    return result
