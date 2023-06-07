#!/usr/bin/python3
def islower(c):
    for lower in c:
        if ord(c) >= 97 and ord(c) <= 122:
            return True
    return False
