#!/usr/bin/python3

"""Unittest for class Base"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_id_None(self):
        b1 = Base(None)
        b2 = Base(None)
        b3 = Base(None)
        self.assertEqual(b2.id, b3.id - 1)

    def test_default_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_two_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_custom_id_assignment(self):
        self.assertEqual(12, Base(12).id)

    def test_id_str(self):
        self.assertEqual("Holberton", Base("Holberton").id)

    def test_id_bool(self):
        self.assertEqual(True, Base(True).id)

    def test_id_int(self):
        self.assertEqual(6, Base(6).id)

    def test_id_float(self):
        self.assertEqual(6.0, Base(6.0).id)

    def test_id_tuple(self):
        self.assertEqual((1, 2, 3), Base((1, 2, 3)).id)

    def test_id_list(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_id_set(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_id_dict(self):
        self.assertEqual({"a": 0, "b": 1}, Base({"a": 0, "b": 1}).id)

    def test_rectangle_case(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertIsInstance(r1, Rectangle)
        self.assertTrue(hasattr(r1, 'id'))
        self.assertEqual(r1.id, 12)
        self.assertTrue(hasattr(r1, 'width'))
        self.assertEqual(r1.width, 10)
        self.assertTrue(hasattr(r1, 'height'))
        self.assertEqual(r1.height, 2)
        self.assertTrue(hasattr(r1, 'x'))
        self.assertEqual(r1.x, 0)
        self.assertTrue(hasattr(r1, 'y'))
        self.assertEqual(r1.y, 0)

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
