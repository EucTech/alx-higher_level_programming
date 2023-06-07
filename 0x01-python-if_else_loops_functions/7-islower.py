#!/usr/bin/python3
def islower(c):
    for lower in c:
        if ord(lower) >= 97 and ord(lower) <= 122:
            return True
        else:
            return False
