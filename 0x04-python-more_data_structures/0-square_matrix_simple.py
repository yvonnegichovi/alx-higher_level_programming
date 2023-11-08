#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    def square_value(value):
        return value ** 2
    new_matrix = list(map(lambda row: list(map(square_value, row)), matrix))
    return new_matrix
