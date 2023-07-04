#!/usr/bin/python3

import requests

url = 'https://alx-intranet.hbtn.io/status'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Display the body of the response
    print(f"Response body:\n{'-' * 50}")
    print(response.text)
    print('-' * 50)
else:
    # Display the error code
    print(f"Error code: {response.status_code}")
