#!/usr/bin/python3
"""
Rotate a 2D matrix by 90 degrees clockwise in place.

This function rotates a square matrix in place by 90 degrees clockwise.

Args:
    matrix (List[List[int]]): The square matrix to rotate.

Returns:
    None
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given square matrix by 90 degrees clockwise in place.
    """
    left = 0
    right = len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top = left
            bottom = right

            # Save the top-left element
            top_left = matrix[top][left + i]

            # Move bottom-left to top-left
            matrix[top][left + i] = matrix[bottom - i][left]

            # Move bottom-right to bottom-left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # Move top-right to bottom-right
            matrix[bottom][right - i] = matrix[top + i][right]

            # Move saved top-left to top-right
            matrix[top + i][right] = top_left

        left += 1
        right -= 1
