#!/usr/bin/python3
"""
Readme the file
"""
def read_file(filename=""):
    """ function to read from file """
    with open(filename, "r", encoding="UTF-8") as file:
        read = file.read()
    print(read, end="")
