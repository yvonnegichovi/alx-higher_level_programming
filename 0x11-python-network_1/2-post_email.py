#!/usr/bin/python3
"""Sends a  POST request to a URL with email as a parameter"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    """Ensures that the code is not executed when imported"""
    url =  sys.argv[1]
    email =  sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(email)
