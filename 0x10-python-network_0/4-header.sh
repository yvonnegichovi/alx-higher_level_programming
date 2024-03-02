#!/bin/bash
# return a GET request with a custom header
curl -sH "X-School-User-Id: 98" "$1"
