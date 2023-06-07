#!/usr/bin/python3
def uppercase(str):
    for upper in str:
        if ord(upper) >= 97 and ord(upper) <= 122:
            alpha = (chr(ord(upper)-32))
        else:
            alpha = upper
        print("{}".format(alpha), end="")
    print()
