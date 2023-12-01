#!/usr/bin/python3

"""This module looks for a couple of characters and add new lines to it"""


def text_indentation(text):
    """This function that prints a text with 2 new lines
    after each of these characters: ., ? and :"""
    s = [".", "?", ":"]
    current_line = ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        current_line += i
        if i in s:
            print(current_line. strip())
            print()
            current_line = ""
    if current_line.strip():
        print(current_line.strip(), end="")
