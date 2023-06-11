#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    new_list = my_list.copy()
    count = 0
    for i in new_list:
        if count == idx:
            new_list[count] = element
        count += 1
    return new_list
