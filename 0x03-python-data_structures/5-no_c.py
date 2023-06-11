#!/usr/bin/python3
def no_c(my_string):
    value = ""
    count = 0
    for i in my_string:
        if i != 'c' and i != 'C':
            value += i
            count += 1
    return value
