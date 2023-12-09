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
        self.__width = value

    @property
    def height(self):
        """This getter method instance retrieves the private instance 
        of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This setter method instance sets the parameters for height"""
        self.__height = value

    @property
    def x(self):
        """This getter method instance retrieves the private instance of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """This setter method instance sets the parameters for x"""
        self.__x = value

    @property
    def y(self):
        """This getter method instance retrieves the private instance of y"""
        return self.__y

    @y.setter
    def x(self, value):
        """This setter method instance sets the parameters for y"""
        self.__y = value
