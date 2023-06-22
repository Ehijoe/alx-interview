#!/usr/bin/python3
"""Island perimeter."""


def safe_get(grid, i, j):
    """Get the value at a cell in a grid without throwing an error."""
    try:
        return grid[i][j]
    except IndexError:
        return 0


def check_borders(cell, grid, i, j):
    """Check if the borders of a cell are on the perimeter."""
    borders = 0
    for off in [1, -1]:
        if cell != safe_get(grid, i + off, j):
            borders += 1
        if cell != safe_get(grid, i, j + off):
            borders += 1
    return borders


def island_perimeter(grid):
    """Calculate the perimeter of an island."""
    perimeter = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:
                perimeter += check_borders(cell, grid, i, j)
    return perimeter
