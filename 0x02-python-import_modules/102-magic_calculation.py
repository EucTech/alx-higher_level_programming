#!/usr/bin/python3
def magic_calculation(a, b):
    add = magic_calculation_102.add
    sub = magic_calculation_102.sub
    if a < b:
        c = add(a, b)
        for j in range(4, 7):
            c = add(c, j)
        return c
    else:
        return sub(a, b)
