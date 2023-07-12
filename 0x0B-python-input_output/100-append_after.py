#!/usr/bin/python3
"""
    a function that inserts a line of text to a file,
    after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """append function"""
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.readlines()

    with open(filename, 'w') as f:
        for i in text:
            f.write(i)
            if search_string in i:
                f.write(new_string)
