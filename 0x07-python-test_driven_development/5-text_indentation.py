#!/usr/bin/python3
"""A function that print a text with 2 new lines after '.','?',':'"""


def text_indentation(text):
    """This is the function that prints text_indentation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if '.' in text:
        text = text.replace('. ', '.\n\n')
    if '?' in text:
        text = text.replace('? ', '?\n\n')
    if ':' in text:
        text = text.replace(': ', ':\n\n')
    print(text.strip())
