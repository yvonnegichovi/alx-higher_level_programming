#!/bin/bash
# returns POST request with custom header
curl -s -H POST "email: test@gmail.com" "subject: I will always be here for PLD" "$1"
