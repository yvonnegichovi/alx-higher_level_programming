#!/bin/bash
# returns POST request with custom header
curl -s -X POST -d "email=test@gmail.com&subject=will always be here for PLD" "$1"
