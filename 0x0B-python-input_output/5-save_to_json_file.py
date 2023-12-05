#!/usr/bin/python3

"""This module write a function that writes an Object to a text file,
using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """This method writes an Object to a text file,
    using a JSON representation"""
    with open(filename, "w", encoding="UTF-8") as file:
        json.dump(my_obj, file)
