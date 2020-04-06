#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def position(self):
        return self.__position

    def position(self, value):
        error = 'position must be a tuple of 2 positive integers'
        if not(isinstance(value, tuple)):
            raise TypeError(error)
        if not(len(value) == 2):
            raise TypeError(error)
        if not(isinstance(value[0], int)):
            raise TypeError(error)
        if not(isinstance(value[1], int)):
            raise TypeError(error)
        if (value[0] < 0 or value[1] < 0):
            raise TypeError(error)
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Print"""
        if self.size > 0:
            if self.position[1] > 0:
                for i in range(self.position[1]):
                    print()
            for j in range(self.size):
                for a in range(self.position[0]):
                    print("_", end="")
                for b in range(self.size):
                    print("#", end="")
                print("$")
        else:
            print()
