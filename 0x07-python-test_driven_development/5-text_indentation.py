#!/usr/bin/python3
"""The text-indentation moudule docstring."""


def text_indentation(text):
    """Inside the function.

    Args:
        text (str): str
    Raise:
        TypeError
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    idx = 0
    while idx < len(text) and text[idx] == " ":
        idx += 1

    while idx < len(text):
        print(text[idx], end="")
        if text[idx] == "\n" or text[idx] in ".?:":
            if text[idx] in ".?:":
                print("\n")

            idx += 1
            while idx < len(text) and text[idx] == ' ':
                idx += 1
            continue
        idx += 1
