#!/usr/bin/python3

import requests
import sys

# Get the URL from command-line arguments
url = sys.argv[1]

# Send a GET request to the URL
response = requests.get(url)

# Check the HTTP status code
if response.status_code >= 400:
    # Print the error code
    print(f"Error code: {response.status_code}")
else:
    # Display the body of the response
    print(f"Response body:\n{'-' * 50}")
    print(response.text)
    print('-' * 50)
