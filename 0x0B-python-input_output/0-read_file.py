#!/usr/bin/python3
"""read_file"""


def read_file(filename=""):
    """create function that read a text file"""
    with open(filename, encoding="UTF8") as f:
        line = f.read()
    print(line, end="")
    f.close()
