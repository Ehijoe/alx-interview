#!/usr/bin/python3
"""A function to build pascal's triangle."""


def generate_row(previous):
    """Generate the next row of a pascal's triangle."""
    if len(previous) == 0:
        return [1]
    row = [1]
    for idx, num in enumerate(previous[1:]):
        row.append(num + previous[idx])
    row.append(1)
    return row


def pascal_triangle(n):
    """Return a pascal's triangle of height n."""
    if n <= 0:
        return list()
    triangle = pascal_triangle(n - 1)
    if len(triangle) == 0:
        prev = []
    else:
        prev = triangle[-1]
    triangle.append(generate_row(prev))
    return triangle
