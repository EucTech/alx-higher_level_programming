#!/usr/bin/python3
def islower(c):
    for lower in range(ord('a'), ord('z') + 1):
        if c == chr(lower):
            return True
    return False
