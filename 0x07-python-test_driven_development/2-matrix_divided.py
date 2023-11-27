#!/usr/bin/python3

"""This module divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix
    while considering certain listed exceptions

    Args:
        matrix (list of list): The input matrix containing int/floats
        div (int/float): The number by which the matrix elements will be divided
    Returns:
        list of list: a new matrix with elements rounded to 2 decimal places
    Raises:
        TypeError:
            If matrix is not a list of lists of integers/floats,
            if each row of the matrix does not have the same size,
            or if div is not a number (integer or float).
        ZeroDivisionError:
            If div is equal to 0.
    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result_matrix = [[round(float(element) / div, 2) for element in row] for row in matrix] 
    return result_matrix
