#!/usr/bin/python3
"""checking for subclass"""


def inherits_from(obj, a_class):
    """inheritance function"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
