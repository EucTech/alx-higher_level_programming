#!/usr/bin/python3
"""
    This is a function that appends a string at the end of a text
    file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """append a text to a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        append_file = f.write(text)
    return append_file
