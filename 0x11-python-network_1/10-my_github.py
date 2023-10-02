#!/usr/bin/python3
"""This is a Python script that takes your GitHub credentials (username
and password) and uses the GitHub API to display your id"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    res = requests.get(url, auth=(username, password))

    res = res.json()
    res = res.get("id")
    print(res)
