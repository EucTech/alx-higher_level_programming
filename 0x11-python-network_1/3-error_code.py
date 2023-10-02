#!/usr/bin/python3
"""This a Python script that takes in a URL, sends a
request to the URL and displays the body of the response
(decoded in utf-8)."""
from urllib.request import Request, urlopen
import sys
from urllib.error import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    request = Request(url)
    try:
        with urlopen(request) as response:
            content  = response.read().decode('utf-8')
            print(content)
    except HTTPError as e:
        print(f"Error code: ", e.code)
