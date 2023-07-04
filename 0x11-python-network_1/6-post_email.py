#!/usr/bin/python3

import requests
import sys

# Get the URL and email from command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Prepare the data to be sent in the POST request
data = {'email': email}

# Send a POST request to the URL with the email as a parameter
response = requests.post(url, data=data)

# Display the body of the response
print(f"Response body:\n{'-' * 50}")
print(response.text)
print('-' * 50)
