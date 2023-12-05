#!/usr/bin/python3

"""This model Returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """Returns tthe JSON representation of an objects(string)"""
    return json.dumps(my_obj)
