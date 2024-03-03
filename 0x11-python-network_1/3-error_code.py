#!/usr/bin/python3
"""Handles url errors"""

from urllib.request import Request, urlopen
import urllib.parse
from urllib.error import URLError, HTTPError
import sys


if __name__ == "__main__":
    """Ensures that the code is not executed when imported"""
    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
