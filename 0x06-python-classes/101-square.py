#!/usr/bin/python3

"""This module defines a square"""


class Square:
    """This class defines the fields and methods of Square class

    private instance attributes:
        size: size of the square
        position: postion of the sizes

    public instance methods:
        def area(self): returns the current square area
        def my_print(self): prints the square using '#' character

    properties:
        def size(self): to retrieve it
        def size(self, value): to set it
        def position(self): to retrieve it
        def position(self, value):

    Instantiation:
        def __init__(self, size=0, position=(0, 0))"""

    def __init__(self, size=0, position=(0, 0)):
        """This method iinitializes size and position objects"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """This getter method retrieves size as a privatized object"""
        return self.__size

    @size.setter
    def size(self, value):
        """This setter method changes the value of size instance"""
        if type(value) is not int:
            raise TypeError("size must be an interger")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """This getter method retrieves position as aprivate instance"""
        return self.__position

    @position.setter
    def position(self, value):
        """This setter method changes teh value of teh postion instance"""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not isinstance(value[0], int) or value[0] < 0 \
                or not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This method returns the area of the Square"""
        return self.__size ** 2

    def my_print(self):
        """This  method prints area in stdout with character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """This method prints the Square class just like my_print"""
        result = ""
        for i in range(self.__position[1]):
            result += "\n"
        for i in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result.rstrip("\n")
