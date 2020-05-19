#!/usr/bin/python3
"""
class basegeometry
"""


class BaseGeometry:
    """
    function area
    """

    def area(self):
        raise Exception("area() is not implemented")

    """
    function integer validator
    """

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        if type(name) is not str:
            raise TypeError("{} must be a string".format(name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
