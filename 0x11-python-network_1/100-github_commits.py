#!/usr/bin/python3
"""This is a cript that print the 10 recent commit message"""
import requests
import sys


if __name__ == "__main__":
    repoName = sys.argv[1]
    ownerName = sys.argv[2]

    # number of commitss that will be print
    perPage = 10

    url =\
        f"https://api.github.com/repos/{ownerName}/{repoName}/commits"

    # "sort" to "committer-date", you ensure that the commits are
    # listed from the newest to the oldest.
    # "per_page": perPage: This parameter specifies the number of commits
    # to be included in each page of the API response
    params = {
        "sort": "committer-date",
        "per_page": perPage
    }

    res = requests.get(url, params=params)
    result = res.json()

    for commit in result:
        sha = commit["sha"]
        authorName = commit["commit"]["author"]["name"]
        print(f"{sha}: {authorName}")
