#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_value = []
    for n, i in a_dictionary.items():
        if i == value:
            delete_value.append(n)
    for n in delete_value:
        del a_dictionary[n]
    return a_dictionary
