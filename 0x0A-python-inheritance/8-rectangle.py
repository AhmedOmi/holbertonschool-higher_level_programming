#!/usr/bin/python3
'''
import my class BaseGeometry
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
