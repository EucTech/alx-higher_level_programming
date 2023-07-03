#!/usr/bin/python3
"""This is rectangle class to get the area and primeter of a rectangle"""


class Rectangle:
    """This is the definion of the class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

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
        """Get the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Get the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rec = ""
        for i in range(self.__height):
            rec += "#" * self.__width
            if i != self.__height - 1:
                rec += "\n"
        return rec

    def __repr__(self):
        """To string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
