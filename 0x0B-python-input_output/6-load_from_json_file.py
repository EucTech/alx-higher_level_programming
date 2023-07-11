#!/usr/bin/python3
"""
    This is a a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """Object file from JSON"""
    with open(filename, 'r', encoding="utf-8") as f:
        objfile = json.load(f)
    return objfile
