#!/usr/bin/python3

"""This module divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix
    while considering certain listed exceptions
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all(isinstance(row, list)for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda row: round(row / div, 2), i)))
    return new_matrix
