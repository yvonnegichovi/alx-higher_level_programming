#!/usr/bin/python3
"""Uses  requests package and displays a variable"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    body = requests.get(url)
    x_request_id = body.headers.get('X-Request-Id')
    print(x_request_id)

