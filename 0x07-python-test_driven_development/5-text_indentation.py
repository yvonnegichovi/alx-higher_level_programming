#!/usr/bin/python3

"""This module looks for a couple of characters and add new lines to it"""


def text_indentation(text):
    """This function that prints a text with 2 new lines
    after each of these characters: ., ? and :"""
    s = [".", "?", ":"]
    current_line = text.split()
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in current_line:
        print(i, end="")
        if not (set(i) and s):
            if not (i == current_line[-1]):
                print(" ", end="")
        if set(i) and s:
            print("\n")
