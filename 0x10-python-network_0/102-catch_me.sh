#!/bin/bash
# makes a request to the web server to respond with a message
curl -s -X POST -H "User-Agent: You got me!" http://0.0.0.0:5000/catch_me
