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

    def my_print(self):
        """This method prints in stdout the square with the # character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
