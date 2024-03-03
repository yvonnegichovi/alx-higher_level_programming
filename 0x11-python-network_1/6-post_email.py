#!/usr/bin/python3
"""sends a POST requests to the URL passed witth an email as a parameter"""

import requests
import sys


if __name__ == "__main__":
    """Ensures that the code is not executed when imported"""
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    body = requests.post(url, data=payload)
    print(body.text)
