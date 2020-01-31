#!/usr/bin/python3
'''
class rectangle inhertis from Base
'''
from models.base import Base


class Rectangle(Base):
    ''' class rectangle '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' funtion constructor '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def x(self):
        ''' function prority '''
        return self.__x

    @property
    def y(self):
        ''' function prority '''
        return self.__y

    @property
    def width(self):
        ''' function prority '''
        return self.__width

    @property
    def height(self):
        ''' function prority '''
        return self.__height

    @x.setter
    def x(self, value):
        ''' function setter '''
        self.__x = value

    @y.setter
    def y(self, value):
        ''' function setter '''
        self.__y = value

    @width.setter
    def width(self, value):
        ''' function setter '''
        self.__width = value

    @height.setter
    def height(self, value):
        ''' function setter '''
        self.__height = value
