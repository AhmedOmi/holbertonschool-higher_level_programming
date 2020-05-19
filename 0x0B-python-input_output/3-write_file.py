#!/usr/bin/python3
"""
write file function
"""


def write_file(filename="", text=""):
    with open(filename, 'w') as file:
        file.write(text)
        return(len(text))