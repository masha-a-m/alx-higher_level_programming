#!/usr/bin/python3

import requests

import sys

# Get the repository name and owner name from command-line arguments
repo_name = sys.argv[1]
owner_name = sys.argv[2]

# Set up the API endpoint URL
url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

# Send a GET request to the GitHub API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the list of commits from the response JSON
    commits = response.json()

    # Iterate over the commits and print them in the desired format
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
else:
    # Display the error code
    print(f"Error code: {response.status_code}")
