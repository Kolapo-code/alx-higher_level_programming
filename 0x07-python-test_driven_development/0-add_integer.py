#!/usr/bin/python3
"""Addition module.



"""
def add_integer(a, b=98):
    """Returns the sum of two ints.
    Raises: TypeError for types besides int and float
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
