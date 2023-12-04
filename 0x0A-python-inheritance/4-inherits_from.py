#!/usr/bin/python3

"""This module checks for an instance in an inherited class"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class inherited
    from the specified class."""
    return type(obj) != a_class and issubclass(type(obj), a_class)
