#!/usr/bin/python3
"""
     This is a function that reads a text file (UTF8)
    and prints it to stdout
"""


def read_file(filename=""):
    """This is the read file"""
    with open(filename, encoding="utf-8") as f:
        for text in f:
            print(text, end="")
