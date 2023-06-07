#!/usr/bin/python3
rev = ""
for alpha in range(122, 96, -1):
    if alpha % 2 == 0:
        rev += chr(alpha)
    else:
        rev += chr(alpha - 32)
print("{}".format(rev), end="")
