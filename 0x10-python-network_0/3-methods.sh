#!/bin/bash
# displays all HTTP methods
curl -sIX OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
