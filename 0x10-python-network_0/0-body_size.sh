#!/bin/bash
#Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the res
curl -s "$1" | wc -c
