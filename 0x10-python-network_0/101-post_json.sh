#!/bin/bash
# sends a JSON POST request and displays the body request
curl -s -b POST "$2" "$1"
