#!/usr/bin/python3
"""Lookup
"""


def lookup(obj):
    '''
the function returns the properties and methods without values
 Args:
        obj: instance of the class
    Returns:
        List of attributes
    '''

    return dir(obj)
