#!/usr/bin/python3

#task python

import requests
import sys

# Get the letter from command-line arguments
letter = sys.argv[1] if len(sys.argv) > 1 else ""

# Prepare the data to be sent in the POST request
data = {'q': letter}

# Send a POST request to the specified URL with the letter as a parameter
response = requests.post('http://0.0.0.0:5000/search_user', data=data)

try:
    # Parse the response as JSON
    json_data = response.json()

    if json_data:
        # Display the id and name
        user = json_data.get('id', None), json_data.get('name', None)
        print(f"[{user[0]}] {user[1]}")
    else:
        # Display "No result" if the JSON is empty
        print("No result")
except ValueError:
    # Display "Not a valid JSON" if the JSON is invalid
    print("Not a valid JSON")
