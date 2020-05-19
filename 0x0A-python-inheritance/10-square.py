#!/usr/bin/python3
"""
import from other file
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
class rectangle inheritance from basegeometry
"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        constructor
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        return Area
        """
        return self.__width * self.__height

    def __str__(self):
        """String function"""
        return "[Rectangle] " + \
            str(self.__width) + "/" + str(self.__height)
