#!/usr/bin/python3
def best_score(a_dictionary):
    n, m = None, None
    if a_dictionary:
        for a, b in a_dictionary.items():
            if not m or b > m:
                n, m = a, b
    return n
