#!/usr/bin/python3

"""Unittest for rectangle.py
Unittest classes:
    TestRectangle_Constructor - line 15
    """

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle_Constructor(unittest.TestCase):
    def test_default_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, r2.id - 1)

    def tset_custom_id_assignement(self):
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(12, r.id)

    def test_width_position(self):
        r = Rectangle(10, 2, 1, 3)
        self.assertEqual(r.width, 10)


class TestRectangle_Validation(unittest.TestCase):
    def test_invalid_height_type(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, "2")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_invalid_width_value(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as context:
            r.width = -10
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_invalid_x_type(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError) as context:
            r.x = {}
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_invalid_y_value(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(context.exception), "y must be >= 0")


if __name__ == '__main__':
    unittest.main()
