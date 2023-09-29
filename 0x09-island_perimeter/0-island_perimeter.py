#!/usr/bin/env python3
"""
island perimeter interview question
"""


def island_perimeter(grid):
    """
    returns perimeter of island
    """
    perimeter = 0

    # Helper function to check if a cell is within the grid boundaries
    def is_valid(x, y):
        """
        check if dimensions are valid
        """
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    # Directions to check for adjacent land cells (up, down, left, right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    bool_1 = is_valid(new_row, new_col)
                    bool_2 = grid[new_row][new_col] == 0
                    if not bool_1 or bool_2:
                        perimeter += 1

    return perimeter
