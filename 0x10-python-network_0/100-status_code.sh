#!/bin/bash
# sends a request to URL and displays only the status cod of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
