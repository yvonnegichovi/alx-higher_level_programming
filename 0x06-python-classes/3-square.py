#!/usr/bin/python3

""" This module defines a square"""


class Square:
    """This class defines the class attribute Square"""
    def __init__(self, size=0):
        """The method initializes the size instance"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """This method returns the current square area"""
        return self.__size * self.__size
