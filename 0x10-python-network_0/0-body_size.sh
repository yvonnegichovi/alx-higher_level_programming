#!/bin/bash
# takes in a URL, sends a request to that URL, and displays size of the body
curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'
