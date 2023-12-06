#!/usr/bin/python3


"""This module creates a class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits form the class BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation of width and height using method init"""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """This method returns a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
