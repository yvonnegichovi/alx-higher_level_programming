#!/usr/bin/python3

"""This module defines a square"""


class Square:
    """This class defines the fields and methods of a Square class"""

    def __init__(self, size=0):
        """This method initializes the size of the Square class"""
        self.size = size

    @property
    def size(self):
        """This getter method retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """This setter method sets the private instance of size

        while considering some conditions"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """This method returns the area of the Square"""
        return self.__size * self.__size

    def __eq__(self, other):
        """checks if the area is equal to other areas"""
        return self.area() == other.area()

    def __ne__(self, other):
        """checks whether the current area is not equal to other area"""
        return self.area() != other.area()

    def __lt__(self, other):
        """checks whether the current area is less than other area"""
        return self.area() < other.area()

    def __le__(self, other):
        """checks whether the current area is less than or
        equal to other area"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """checks whether the current area is greater to other area"""
        return self.area() > other.area()

    def __ge__(self, other):
        """checks whether the current area is greater or equal
        to other areas"""
        return self.area() >= other.area()
