#!/usr/bin/python3

def append_write(filename="", text=""):
    """This method appends a string at the end of a text file
    and returns the number of characters added
    must use with statement to open the file
    must use encoding UTF8
    """
    with open(filename, "a", encoding="UTF-8") as file:
        text_added = file.write(text)
    return text_added
