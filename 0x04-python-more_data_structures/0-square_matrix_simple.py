#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[m[count]**2 for count in range(len(m))] for m in matrix]
