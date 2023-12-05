#!/usr/bin/python3

"""This module reads a text and pprints it to stdout"""


def read_file(filename=""):
    """This method uses with to  open and  read a file
    while printing its text to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
