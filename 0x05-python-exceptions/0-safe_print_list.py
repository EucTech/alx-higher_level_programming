#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        val = 0
        for ele in range(x):
            print("{}".format(my_list[ele]), end="")
            val += 1
        print()
    except IndexError:
        pass
        print()
    return val
