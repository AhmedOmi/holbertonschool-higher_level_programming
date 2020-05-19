#!/usr/bin/python3
"""
read the n  line in the file
"""


def read_lines(filename="", nb_lines=0):
    """ function to read nb_lines from file """
    with open(filename, "r", encoding="UTF-8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")

        else:
            for line in file:
                print(line, end="")
