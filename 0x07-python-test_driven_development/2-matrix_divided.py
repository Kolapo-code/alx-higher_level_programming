#!/usr/bin/python3
"""Matrix division module."""


def matrix_divided(matrix, div):
    """Matrix division func.

    Args:
        matrix (list[list[int]]): list of list of ints or floats.
        div (int): int or float divisor

    Raises:
        TypError and ZeroDivisionError
    Return:

        Divided matrix
    """
    if (not isinstance(matrix, list)
            or not all(map(lambda x: isinstance(x, list), matrix))
            or not all([all(map(lambda y: isinstance(y, int) or isinstance(y, float), x)) for x in matrix])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(map(lambda x: len(x) == len(matrix[-1]), matrix)):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
