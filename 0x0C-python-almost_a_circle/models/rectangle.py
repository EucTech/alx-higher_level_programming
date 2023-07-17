#!/usr/bin/python3
"""
    A rectangle class that inherits from base
"""
import sys
import json
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """To display"""
        rec = ""
        for _ in range(self.y):
            rec += "\n"
        for i in range(self.__height):
            rec += ' ' * self.x + "#" * self.__width
            if i != self.__height - 1:
                rec += "\n"
        print(rec, file=sys.stdout)
        return rec

    def __str__(self):
        """string repr"""
        return f"[Rectangle] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """A public method that assigns an argument to each attribute"""
        attr = ['id', 'width', 'height', 'x', 'y']
        if args:
            index = 0
            for i in args:
                setattr(self, attr[index], i)
                index += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
        return self.__str__()

    def to_dictionary(self):
        """Return the dictionary"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
