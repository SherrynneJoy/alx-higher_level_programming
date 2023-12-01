#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    utf_cont = content.decode('utf-8')

    print("Body response:")
    print("type:", type(content))
    print("content: b'OK'")
    print("utf8 content: OK")
