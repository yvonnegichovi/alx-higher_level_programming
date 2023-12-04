#!/usr/bin/python3

"""This module returns the list of available attributes
and methods of an object"""


def lookup(obj):
    """This method returns available attributes and methods of
    the object called"""
    return dir(obj)
