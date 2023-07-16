#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """inherits Rectangle instantiation"""
        self.size = size
        """assigning height and width to size"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """To return the width"""
        return self.width

    @size.setter
    def size(self, value):
        """set the value of width and height to same value"""
        self.width = value
        self.height = value
