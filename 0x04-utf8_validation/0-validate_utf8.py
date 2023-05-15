#!/usr/bin/python3
"""Validate a utf-8 string."""


def validUTF8(data):
    """Validate a utf-8 string."""
    extra_bytes = 0
    for byte in data:
        if extra_bytes > 0 and ((byte ^ 0b10000000) & 0b11000000) == 192:
            return False
        elif extra_bytes > 0:
            extra_bytes -= 1
        else:
            leading_ones = 0
            while (byte & 0b10000000) != 0:
                byte = byte << 1
                leading_ones += 1
            if leading_ones not in [0, 2, 3, 4]:
                return False
            elif leading_ones > 0:
                extra_bytes = leading_ones - 1
    return (extra_bytes == 0)
