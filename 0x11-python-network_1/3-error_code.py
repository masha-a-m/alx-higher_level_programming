#!/usr/bin/python3

import urllib.request
import sys
import urllib.error

# Get the URL from command-line arguments
url = sys.argv[1]

try:
    # Send a request to the URL
    with urllib.request.urlopen(url) as response:
        # Read the response data
        body = response.read().decode('utf-8')

    # Display the body of the response
    print(f"Response body:\n{'-' * 50}\n{body}\n{'-' * 50}")

except urllib.error.HTTPError as e:
    # Handle HTTPError exceptions
    print(f"Error code: {e.code}")
