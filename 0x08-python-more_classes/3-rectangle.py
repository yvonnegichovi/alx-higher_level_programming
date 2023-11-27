#!/usr/bin/python3

"""This module defines a Square class."""


class Rectangle:
    """class Rectangle has the following attributes:

    private instance attributes:
        1. width
        2. height

    public instance attributes:
        1. def area(self):
        2. def perimeter(self):

    property:
        1. def width(self): to retrieve it
        2. def height(self): to retrieve it

    propert setters:
        1. def width(self, value): to set it
        2. def height(self, value)

    instantation:
        def __init__(self, width=0, height=0):
    """
    def __init__(self, width=0, height=0):
        """method: init that initializes width and height instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """This getter method retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This setter method sets the private width instance attribute
        considering the metioned situations"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This getter method retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This setter method sets the private height instance attribute
        while considering certain exceptions shown below"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This public instance method returns the rectangular area"""
        return self.__width * self.__height

    def perimeter(self):
        """This public einstance method returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """This str method prints the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(['#' * self.width for _ in range(self.height)])
