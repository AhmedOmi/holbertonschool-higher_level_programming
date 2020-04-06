
#!/usr/bin/python3
class Square:
    """class square
    """

    def __init__(self, size=0, position=(0, 0)):
        """square class constructor
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """size function
        """
        return self.__size

    @size.setter
    def size(self, value):
        """square size setter function.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """square position function
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set square position
        """
        if (
                not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                (value[0] < 0 or value[1] < 0)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate the square area.
        """
        return self.__size ** 2

    def my_print(self):
        """print function."""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for l in range(self.position[1]):
                    print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
