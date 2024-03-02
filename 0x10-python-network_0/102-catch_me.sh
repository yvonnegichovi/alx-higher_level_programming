#!/bin/bash
# makes a request to the web server to respond with a message
curl -s -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool"
