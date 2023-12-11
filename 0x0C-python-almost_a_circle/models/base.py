#!/usr/bin/python3

"""This module creates the 'bases' for all other classes in the project
it mwnages id attribute in all the future classes and avoid duplicating
the same code
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string rep of list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as file:
            file.write(json_string)