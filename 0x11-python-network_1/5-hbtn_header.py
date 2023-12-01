#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        r = requests.get(url)
        content = r.headers['X-Request-Id']
        print(content)
    except requests.RequestException as e:
        print(f"Error: {e}")
