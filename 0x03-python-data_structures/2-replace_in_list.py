#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    else:
        count = 0
        for i in my_list:
            if count == idx:
                my_list[count] = element
                return my_list
            count += 1
