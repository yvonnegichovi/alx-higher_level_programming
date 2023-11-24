#!/usr/bin/python3

"""This module prints a square with character #"""


def print_square(size):
    """This function prints a square and raises various errors with messages"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
