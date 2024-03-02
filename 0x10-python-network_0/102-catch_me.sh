#!/bin/bash
# makes a request to the web server to respond with a message
curl -s -o /dev/null -w "You got me!" 0.0.0.0:5000/catch_me
