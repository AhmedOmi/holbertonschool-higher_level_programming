#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ find_peak function """
    list = list_of_integers.sort()
    return list[1]
