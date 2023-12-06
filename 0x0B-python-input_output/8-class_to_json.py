#!/usr/bin/python3


""" This module  returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """obj isan instance of a Class"""
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
        for key, value in obj.__dict__.items():
            if hasattr(value, "__dict__"):
                result[key] = class_to_obj(value)
        return result
    elif hasattr(obj, "__iter__"):
        return [class_to_join(item) for item in obj]
    else:
        return obj
