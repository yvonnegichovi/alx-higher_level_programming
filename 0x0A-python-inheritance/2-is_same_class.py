#!/usr/bin/python3

""" This module return true or false"""


def is_same_class(obj, a_class):
    """ This method returns True if the object is exactly an instance
    of the specified class ; otherwise False."""
    return type(obj) == a_class
