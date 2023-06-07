#!/usr/bin/python3
"""Rotatate a matrix."""


def rotate_2d_matrix(matrix):
    """Rotate a 2d matrix."""
    # Transpose the matrix
    matrix_copy = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    for i, row in enumerate(matrix):
        matrix[i] = matrix_copy[i]
    # Flip the matrix
    for row in matrix:
        row.reverse()
    return matrix
