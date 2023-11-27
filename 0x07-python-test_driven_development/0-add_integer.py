#!/usr/bin/python3

"""This module adds two intergers"""


def add_integer(a, b=98):
    """This function adds two intergers
    and if floats they have to be casted into intergers first"""

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
