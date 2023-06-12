#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_number = 0
    for i in my_list:
        num = int(i)
        if num > max_number:
            max_number = num
    return max_number
