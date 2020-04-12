#!/usr/bin/python3
"""
Only sub class of
"""


def inherits_from(obj, a_class):
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
