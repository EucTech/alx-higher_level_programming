#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    length = len(sys.argv)-1
    if length == 0:
        print(f"{length}")
    if length > 0:
        for i in range(1, length + 1):
            sum += int(sys.argv[i])
        print(sum)
