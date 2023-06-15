#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

    result = 0
    prev = 0
    for n in reversed(roman_string):
        val = roman.get(n, 0)

        if val >= prev:
            result += val
        else:
            result -= val

        prev = val
    return result
