#!/usr/bin/python3

"""Unittest for square.py
Unittest classes:
    TestRectangle_Constructor - line 15
    """

import unittest
import os
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_Constructor(unittest.TestCase):
    def test_square_id(self):
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual(s1.id, s2.id - 1)

    def test_square_custom_id_assignement(self):
        s = Square(3, 1, 3, 12)
        self.assertEqual(12, s.id)

    def test_size_position(self):
        s = Square(3, 1, 3, 12)
        self.assertEqual(s.size, 3)


class TestSquare_Validation(unittest.TestCase):
    def test_invalid_size_type(self):
        with self.assertRaises(TypeError) as context:
            Square("2")
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_invalid_size_type_str(self):
        with self.assertRaises(TypeError) as context:
            Square("Two")
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_invalid_size_type_tuple(self):
        with self.assertRaises(TypeError) as context:
            Square((1, 2, 3))
        self.assertEqual(str(context.exception), "width must be an integer")
