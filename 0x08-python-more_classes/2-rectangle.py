#!/usr/bin/python3
"""This is rectangle class to get the area and primeter of a rectangle"""


class Rectangle:
    """This is the definion of the class"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)
        
        if self.width or self.height == 0:
            return 0
