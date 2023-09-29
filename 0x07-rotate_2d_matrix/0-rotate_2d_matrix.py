#!/usr/bin/python3
"""
2D Matrix Rotation
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.
    """
    # Determine the size of the matrix
    n = len(matrix)

    # Transpose the matrix (reflect over its main diagonal)
    for i in range(n):
        for j in range(i, n):
            # Swap elements at (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the clockwise rotation
    for i in range(n):
        matrix[i] = matrix[i][::-1]
