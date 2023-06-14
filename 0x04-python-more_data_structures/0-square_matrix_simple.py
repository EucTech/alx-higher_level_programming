#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        row2 = []
        for num in i:
            value = num ** 2
            row2.append(value)
        new_matrix.append(row2)
    return new_matrix
