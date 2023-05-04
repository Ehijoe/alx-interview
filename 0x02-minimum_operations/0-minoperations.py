#!/usr/bin/python3
"""Function to find the minimum number of operations."""


def minOperations(n: int) -> int:
    """Find the minimum number of copy and paste operations to fill a file."""
    if n < 1:
        return 0
    ops = 0
    div = 2
    while n >= div:
        if n % div == 0:
            n = n // div
            ops += div
        else:
            div += 1
    if ops == 0 and n > 1:
        return n
    return ops
