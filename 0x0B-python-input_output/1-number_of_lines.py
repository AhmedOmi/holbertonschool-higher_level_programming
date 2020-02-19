#!/usr/bin/python3
"""
what is the number of line in the file
"""


def number_of_lines(filename=""):
    """ function to return number of line from file """
    with open(filename, "r", encoding="UTF-8") as file:
        return len(file.readlines())
