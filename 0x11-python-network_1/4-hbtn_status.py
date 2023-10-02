#!/usr/bin/python3
"""This is a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    r = requests.\
            get('https://alx-intranet.hbtn.io/status', auth=('user', 'pass'))

    print("Body response:")
    print(f"\t- type:", type(r.text))
    print(f"\t- content:", r.text)
