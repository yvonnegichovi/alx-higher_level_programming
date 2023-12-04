#!/usr/bin/python3

"""This module checks if an object is an instance of, or if the object
is an instance of a class that inherited from, the specified class;
otherwise False"""


def is_kind_of_class(obj, a_class):
    """This method checks for the instance of an object"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
