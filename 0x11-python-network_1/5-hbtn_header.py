#!/usr/bin/python3

import requests
import sys

# Get the URL from command-line arguments
url = sys.argv[1]

# Send a GET request to the URL
response = requests.get(url)

# Get the value of the X-Request-Id variable from the response header
x_request_id = response.headers.get('X-Request-Id')

# Display the value of the X-Request-Id variable
print(f"X-Request-Id: {x_request_id}")
