#!/usr/bin/python3
"""Sends a  POST request to a URL with email as a parameter"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys


if __name__ == "__main__":
    """Ensures that the code is not executed when imported"""
    url = sys.argv[1]
    email = sys.argv[2]
    data = urlencode({'email': email}).encode('utf-8')
    req = Request(url, data=data)
    with urlopen(req) as response:
        body = response.read()
    print(body.decode("utf-8"))
