#!/usr/bin/python3

"""This module solves the Nqueens puzzle"""

import sys


def is_safe(board, row, col, n):
    """It checks if there's a queen in the same column"""
    for i in range(row):
        if board[i] == col or board[i] - i == col - row \
                or board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n, solutions):
    """The method solves the queens"""
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)


def print_solutions(solutions):
    """This method prints the possible solutions"""
    for solution in solutions:
        print(solution)
    print()


def main():
    """The main method that runs the program"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * N
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
