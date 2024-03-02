#!/bin/bash
# returns POST request with custom header
curl -s -H -b POST "email: test@gmail.com" "subject: I will always be here for PLD" "$1"
