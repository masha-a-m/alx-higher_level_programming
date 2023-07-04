#!/usr/bin/python3

#Write a Python script that fetches https://alx-intranet.hbtn.io/status

if __name__ == '__main__':

#pyton 0x11 
    import urllib.request
    urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:

url = 'https://alx-intranet.hbtn.io/status'

# Fetch the URL
with urllib.request.urlopen(url) as response:
    # Read the response data
    body = response.read().decode('utf-8')

# Display the body of the response
print(f"Response body:\n{'-' * 50}\n{body}\n{'-' * 50}")content = res.read()
