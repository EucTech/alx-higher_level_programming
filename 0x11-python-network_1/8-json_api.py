#!/usr/bin/python3
"""This is a a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'

    data = {'q': q}

    try:
        r = requests.post(url, data)
        r = r.json()

        if r:
            getId = r.get("id")
            getName = r.get("name")
            print(f"[{getId}] {getName}")
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
