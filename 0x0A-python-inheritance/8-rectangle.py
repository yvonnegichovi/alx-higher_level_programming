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
