#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        val = 0
        for ele in my_list:
            print("{}".format(ele), end="")
            val += 1
            if val == x:
                break
        print()
    except IndexError:
        pass
    return val
