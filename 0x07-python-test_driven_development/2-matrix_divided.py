#!/usr/bin/python3
"""A function that divides all the Elments of a matrix"""


def matrix_divided(matrix, div):
    """
        Matrix function

        Args: matrix / div

    """
    if matrix == [] or not (isinstance(matrix, list)) or\
            not all(isinstance(row, list) for row in matrix) or\
            not all(isinstance(va, (int, float))
                    for row in matrix for va in row):
        raise TypeError(
           "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        value = []
        for va in row:
            value.append(round(va / div, 2))
        new_matrix.append(value)
    return new_matrix
