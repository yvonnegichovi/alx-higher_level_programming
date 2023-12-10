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

