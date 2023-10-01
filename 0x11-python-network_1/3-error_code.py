#!/usr/bin/python3
"""This a Python script that takes in a URL, sends a
request to the URL and displays the body of the response
(decoded in utf-8)."""
from urllib.request import Request, urlopen
import sys
from urllib.error import HTTPError


if __name__ == "__main__":
    request = Request(sys.argv[1])
    try:
        response = urlopen(request)
    except HTTPError as e:
        print("Error code: ", e.code)
