#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    multiply_list = []
    second = []

    for n in my_list:
        multiply_tuple = n[0] * n[1]
        multiply_list.append(multiply_tuple)
        second.append(n[1])

    result = sum(multiply_list) / sum(second)
    return result
