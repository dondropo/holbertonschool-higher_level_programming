#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    >>> matrix_divided([[1.0, 3.1], [4.3, -5.3, -6.2]], 1)
    Traceback (most recent call last):
    TypeError: Each row of the matrix must have the same size
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_mtx = []
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    for column in matrix:
        if len(column) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if isinstance(len(column), (int, float)):
            tmp_list = list(map(lambda row: round(row / div, 2), column))
            new_mtx.append(tmp_list)
        else:
            raise TypeError(msg)

    return new_mtx
