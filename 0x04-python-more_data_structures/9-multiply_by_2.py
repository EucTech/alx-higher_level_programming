#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for n, i in new_dict.items():
        new_dict[n] = i * 2
    return new_dict
