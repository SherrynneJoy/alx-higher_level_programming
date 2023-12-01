#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    try:
        content = "email=" + urllib.request.quote(email)
        content = content.encode('utf-8')
        req = urllib.request.Request(url, content)
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
    except Exception as e:
        print('Error code: ', e.code)
