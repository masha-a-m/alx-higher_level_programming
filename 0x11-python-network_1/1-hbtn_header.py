#!/usr/bin/python3


import urllib.request
import sys

# Get the URL from command-line arguments
url = sys.argv[1]

# Send a request to the URL
req = urllib.request.Request(url)

# Fetch the URL
with urllib.request.urlopen(req) as response:
    # Get the value of the X-Request-Id variable from the header
    x_request_id = response.headers.get('X-Request-Id')

# Display the value of the X-Request-Id variable
print(f"X-Request-Id: {x_request_id}")
