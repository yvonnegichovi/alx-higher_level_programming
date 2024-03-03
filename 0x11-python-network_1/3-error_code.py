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
        response = urlopen(req)
    except HTTPError as e:
        print("Error code: {}".format(e))
