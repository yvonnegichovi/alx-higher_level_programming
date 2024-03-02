#!/bin/bash
# sends a JSON POST request and displays the body request
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
