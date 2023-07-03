#!/usr/bin/python3
"""This is a class rectangle"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """intantiate an object width and height"""
        self.__width = width
        self.__height = height

    @property
    #"""This is get the width value"""
    def width(self):
        return self.__width

    @width.setter
    #"""This is the set width to value"""
    def width(self, value):
        self.__width = value

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    #"""This gets the height"""
    def height(self):
        return self.__height

    @height.setter
    #"""This is sets the height to value"""
    def height(self, value):
        self.__height = value

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
