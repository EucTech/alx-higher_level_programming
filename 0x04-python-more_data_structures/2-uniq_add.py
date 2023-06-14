#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    set_num = set()
    for n in my_list:
        if isinstance(n, int) and n not in set_num:
            sum += n
            set_num.add(n)
    return sum
