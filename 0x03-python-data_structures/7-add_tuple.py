#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)

    sum_a = a[0] + b[0]
    sum_b = a[1] + b[1]

    return (sum_a, sum_b)
