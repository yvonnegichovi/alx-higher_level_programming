#!/usr/bin/python3

"""This module adds a class Square and prints its area"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class calculates and returns the area of a square"""
    def __init__(self, size):
        """Initailizes size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the square"""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)
