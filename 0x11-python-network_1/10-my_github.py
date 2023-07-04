#!/usr/bin/python3

import requests
import sys

# Get the username and personal access token from command-line arguments
username = sys.argv[1]
password = sys.argv[2]

# Set up the API endpoint URL
url = 'https://api.github.com/user'

# Send a GET request to the GitHub API with Basic Authentication
response = requests.get(url, auth=(username, password))

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the user ID from the response JSON
    user_id = response.json().get('id')
    # Display the user ID
    print(f"Your GitHub user ID: {user_id}")
else:
    # Display the error code
    print(f"Error code: {response.status_code}")
