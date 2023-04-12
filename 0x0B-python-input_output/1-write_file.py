#!/usr/bin/python3
"""number_of_lines
"""

def write_file(filename="", text=""):
    """Takes in str filename to read the number of lines
    """

    with open(filename, encoding="utf-8") as rea:
        line = rea.write(text)
        return len(line)
