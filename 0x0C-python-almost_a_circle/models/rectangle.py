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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        ''' function setter '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @width.setter
    def width(self, value):
        ''' function setter '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        ''' function setter '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        ''' function to calculate area if rectangle '''
        air = self.width * self.height
        return air

    def display(self):
        ''' function to desplay '''
        for i in range(self.height):
            print("#" * self.width)
