#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
'''
import my class BaseGeometry
'''


class Rectangle(BaseGeometry):
    ''' class Rectangle
    '''

    def __init__(self, width, height):
        ''' init function constructor
        '''

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
