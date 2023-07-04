#!/usr/bin/python3

import urllib.request
import urllib.parse
import sys

# Get the URL and email from command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Prepare the data to be sent in the POST request
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

# Send a POST request to the URL with the email as a parameter
req = urllib.request.Request(url, data=data, method='POST')

# Fetch the URL
with urllib.request.urlopen(req) as response:
    # Read the response data
    body = response.read().decode('utf-8')

# Display the body of the response
print(f"Response body:\n{'-' * 50}\n{body}\n{'-' * 50}")
