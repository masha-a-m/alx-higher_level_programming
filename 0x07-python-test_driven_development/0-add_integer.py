#!/usr/bin/python3
def add_integer(a, b=98):
    # Check if both a and b are integers or floats
    if not (isinstance(a, int) or isinstance(a, float)) or not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # a and b to integers if they are floats
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    # Add integers to return the result
    return a + b
