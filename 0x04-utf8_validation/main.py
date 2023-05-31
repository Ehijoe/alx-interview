#!/usr/bin/python3
"""
Main file for testing
"""

def print_data(data):
    print(" ".join(["{:08b}".format(byte) for byte in data]))

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print_data(data)
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print_data(data)
print(validUTF8(data))

data = [229, 65, 127, 256]
print_data(data)
print(validUTF8(data))
