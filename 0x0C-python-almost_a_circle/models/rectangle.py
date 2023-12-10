#!/usr/bin/python3

""" This module has class Rectangle
It inherits from class Base"""

from models.base import Base


class Rectangle(Base):
    """This class inherits from Base.
    Has private instance attributes each with its own public getter and setter
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """This class constructor initializes private instance attribute
        width, height, x, y, and id"""
        self.width = width
        self.height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """This getter method instance retrieves the private instance
        of width """
        return self.__width

    @width.setter
    def width(self, value):
        """This setter method sets the parameters for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This getter method instance retrieves the private instance 
        of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This setter method instance sets the parameters for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This getter method instance retrieves the private instance of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """This setter method instance sets the parameters for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This getter method instance retrieves the private instance of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """This setter method instance sets the parameters for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This method returns the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdot the Rectangle with character #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """returns str of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """This method assigns an argument to each attribute"""
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.__width = args[1]
        if num_args >= 3:
            self.__height = args[2]
        if num_args >= 4:
            self.__x = args[3]
        if num_args >= 5:
            self.__y = args[4]
