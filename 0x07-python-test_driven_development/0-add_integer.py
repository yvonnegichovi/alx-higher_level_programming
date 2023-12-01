#!/usr/bin/python3

"""This module adds two intergers"""


def add_integer(a, b=98):
    """This function adds two intergers
    and if floats they have to be casted into intergers first
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
