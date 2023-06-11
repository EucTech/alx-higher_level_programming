#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for cnt in range(len(my_list)-1, -1, -1):
        if my_list[cnt] != 0:
            print("{:d}".format(my_list[cnt]))
