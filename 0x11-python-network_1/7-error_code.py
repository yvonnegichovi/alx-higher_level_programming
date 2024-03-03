#!/usr/bin/python3
"""Handles HTML errors when using requests"""


import requests
import sys


if "__name__" == "__main__":
    """Ensures that the code is not executed when imported"""
    url = sys.argv[1]
    body = requests.get(url)
    if body.status_code <= 400:
        print(body.text)
    else:
        print("Error code:", body.status_code)
