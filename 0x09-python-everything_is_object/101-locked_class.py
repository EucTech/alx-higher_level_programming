#!/usr/bin/python3
"""
    This is a class that those not allow user
    to dynamically adding new instance attribute
    to an object
"""


class LockedClass:
    """This the class for LockedClass"""
    __slots__ = ['first_name']
