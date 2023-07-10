#!/usr/bin/python3
"""Base Geometry"""

class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """The area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        """integer validator function"""
        if not isinstance(self.value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
