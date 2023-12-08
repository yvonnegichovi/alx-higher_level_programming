#!/usr/bin/python3

"""This module creates the 'bases' for all other classes in the project
it mwnages id attribute in all the future classes and avoid duplicating
the same code
"""


class Base:
    """This class has a private attribute that counts the id"""
    __nb_objects = 0
    def __init__(self, id=None):
        """This is a class constructor that tracks id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
