#!/usr/bin/python3
class BaseGeometry:
    """
    Integer validator
    """
    def area(self):
        """
        function area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function integer validator
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")