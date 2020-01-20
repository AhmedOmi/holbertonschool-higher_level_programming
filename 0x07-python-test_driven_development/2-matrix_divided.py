#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError("matrix must be a matrix" +
                            "(list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix" +
                            "must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix" +
                                "(list of lists)of integers/floats")
    return [[round(i / div, 2) for i in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
