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
        """string repr"""
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

    def update(self, *args, **kwargs):
        """A public method that assigns an argument to each attribute"""
        attr = ['id', 'size', 'x', 'y']
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
        """Returns dictionary representation of Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
