#!/usr/bin/python3
"""
class MyInt that inherits from int
"""


class MyInt(int):
    def __eq__(self, value):
        return super().__int__() != value

    def __ne__(self, value):
        return super().__int__() == value
