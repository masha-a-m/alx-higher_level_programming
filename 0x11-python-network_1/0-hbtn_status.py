#!/usr/bin/python3

#Write a Python script that fetches https://alx-intranet.hbtn.io/status

if __name__ == '__main__':

#pyton 0x11 
    import urllib.request
    urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
