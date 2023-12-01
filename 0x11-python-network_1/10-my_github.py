#!/usr/bin/python3
"""a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://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/SherrynneJoy"

    try:
        r = requests.get(url, auth=HTTPBasicAuth(username, password))
        r.raise_for_status()

        my_info = r.json()
        print("", my_info['id'])
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
