#!/usr/bin/python3
"""
    a function that returns True if the object is exactly an
    instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """is_same_class function"""
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        False
