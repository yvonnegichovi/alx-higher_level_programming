#!/usr/bin/python3

"""This module prints a string with input"""


def say_my_name(first_name, last_name=""):
    """This function prints a string
    It checks if the names given are a string"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
