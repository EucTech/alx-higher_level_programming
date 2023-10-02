#!/usr/bin/python3
"""This is a Python script that takes in a URL, sends a request to the
URL and displays the body of the response."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        res = requests.get(url, auth=('user', 'pass'))
        res.raise_for_status()

        print(res.text)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code >= 400:
            print(f"Error code: {e.response.status_code}")
