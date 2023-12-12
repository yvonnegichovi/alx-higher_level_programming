#!/usr/bin/python3

"""This module writes class Square and inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class super calls id, x, y, width and height.
    inherits and uses attributes of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor that super calls and uses attrinutes of Rectangle
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """This getter method gets size"""
        return self.width

    @size.setter
    def size(self, value):
        """This setter method sets the attribute size"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns str of the rectangle"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """assigns attributes using args and kwargs"""
        if args:
            arg_name = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, arg_name[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """This method returns the dictionary representation of the Square"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.width,
            'y': self.y
        }

    def __eq__(self, other):
        """Compares attributes"""
        if not isinstance(other, Square):
            return False
        return all(getattr(self, attr) == getattr(
            other, attr) for attr in ['id', 'size', 'x', 'y'])
