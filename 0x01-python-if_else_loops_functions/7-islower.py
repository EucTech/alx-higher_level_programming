#!/usr/bin/python3
def islower(c):
    """checking for lower case"""
    for lower in c:
        if ord(lower) >= 97 and ord(lower) <= 122:
            return True
        else:
            return False
