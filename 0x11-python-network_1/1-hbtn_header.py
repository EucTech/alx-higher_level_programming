#!/usr/bin/python3
"""This is a  Python script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id variable
found in the header of the response."""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.headers
        get_header = headers.get('X-Request-Id')

    print(get_header)
