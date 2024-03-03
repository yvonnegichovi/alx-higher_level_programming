#!/usr/bin/python3
"""fetches an URL using requests package only"""

import requests


if __name__ == "__main__":
    """This ensures that the code is not executed when imported"""
    url = "https://alx-intranet.hbtn.io/status"
    body = requests.get(url)
    print("Body response:")
    print("\t- type:", type(body.text))
    print("\t- content:", body.text)
