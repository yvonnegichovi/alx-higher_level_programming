#!/usr/bin/python3

"""Unittest for class Base"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_default_id_increment(self):
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertTrue(hasattr(b1, 'id'))
        self.assertEqual(b1.id, 1)

        b2 = Base(None)
        b3 = Base(None)
        self.assertEqual(b2.id, b3.id - 1)

        b4 = Base()
        b5 = Base()
        b6 = Base()
        self.assertEqual(b4.id, b6.id - 2)

    def test_custom_id_assignment(self):
        b1 = Base(12)
        self.assertIsInstance(b1, Base)
        self.assertTrue(hasattr(b1, 'id'))
        self.assertEqual(b1.id, 12)
        b2 = Base(12)
        self.assertIsInstance(b2, Base)
        self.assertTrue(hasattr(b2, 'id'))
        self.assertEqual(b2.id, 12)

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
