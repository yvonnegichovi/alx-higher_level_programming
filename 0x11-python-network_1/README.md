0x11. Python - Network #1
Description
This repository contains Python scripts that demonstrate various networking concepts such as making HTTP requests, handling responses, and interacting with APIs using the urllib and requests packages.

Learning Objectives
Fetching internet resources with the Python package urllib
Decoding urllib body response
Using the Python package requests for simpler HTTP requests
Making HTTP GET, POST, PUT, etc. requests
Fetching JSON resources
Manipulating data from an external service
Requirements
Allowed editors: vi, vim, emacs
All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All files should end with a new line
The first line of all files should be exactly #!/usr/bin/python3
A README.md file at the root of the repository, containing a description of the repository
Your code should use pycodestyle (version 2.8.*) and the length of your files will be tested using wc
All your files must be executable
All your modules should have documentation (use python3 -c 'print(__import__("my_module").__doc__)')
You must use get to access dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Your code should not be executed when imported (by using if __name__ == "__main__":)
Tasks
What's my status? #0

Write a Python script that fetches https://alx-intranet.hbtn.io/status using urllib.
Response header value #0

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response using urllib.
POST an email #0

Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8) using urllib.
Error code #0

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8). Handle urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code.
What's my status? #1

Write a Python script that fetches https://alx-intranet.hbtn.io/status using requests.
Response header value #1

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header using requests.
POST an email #1

Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response using requests.
Error code #1

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response using requests. If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code.
Search API

Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter using requests.
My GitHub!

Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id.
