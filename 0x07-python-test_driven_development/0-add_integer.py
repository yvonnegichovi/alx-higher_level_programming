#!/usr/bin/python3

"""This module adds two intergers"""


def add_integer(a, b=98):
    """This function adds two intergers
    and if floats they have to be casted into intergers first

    Args:
        a and b which must be int or floats
    Returns:
        an integer: the addition of a and b
    Raises:
        TypeError: if a nad are not int/floats
    Examples:
        >>> print(add_integer(1, 2))
        3
        >>> print(add_integer(100, -2))
        98
        >>> print(add_integer(2))
        100
        >>> print(add_integer(100.3, -2))
        98
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
