#!/usr/bin/python3

""" This module return true or false"""


def is_same_class(obj, a_class):
    """ This method returns True if the object is exactly an instance
    of the specified class ; otherwise False."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
