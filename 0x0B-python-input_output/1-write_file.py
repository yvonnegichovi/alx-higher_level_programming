#!/usr/bin/python3

"""This module writes a sstring to a text and returrns the no. of chars
written"""


def write_file(filename="", text=""):
    """Wrutes a string to a text file and returns the noo of chars
    written
    Must use with for opening the file
    """
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text)
        return len(text)
