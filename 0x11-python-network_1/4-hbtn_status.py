#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    content = r.text
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
