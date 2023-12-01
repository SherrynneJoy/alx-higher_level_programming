#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)."""
import sys
import urllib.request
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
