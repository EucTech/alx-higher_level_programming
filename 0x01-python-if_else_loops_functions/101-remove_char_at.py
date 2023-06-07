#!/usr/bin/python3
def remove_char_at(str, n):
    value = ""
    for a, remove_char in enumerate(str):
        if a != n:
            value += remove_char
    return value
