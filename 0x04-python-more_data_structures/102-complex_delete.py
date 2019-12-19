#!/usr/bin/python3
def complex_delete(my_dict, value):
    new = {a: b for a, b in my_dict.items() if b == value}
    for key in new:
        my_dict.pop(key)
    return my_dict
