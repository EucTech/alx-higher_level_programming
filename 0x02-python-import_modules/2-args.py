#!/usr/bin/python3
import sys
length = len(sys.argv)-1
count = 0
if length == 0:
    print("0 arguments.")
elif length == 1:
    print("1 argument:")
    for i in range(1, length):
        print("{}: {}".format(length, sys.argv[i]))
elif length > 1:
    print("{} arguments:".format(length))
    for i in range(1, length + 1):
        print("{}: {}".format(i, sys.argv[i]))
