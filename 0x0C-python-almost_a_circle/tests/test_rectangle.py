#!/usr/bin/python3

"""Unittest for rectangle.py
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


class TestRectangle_Constructor(unittest.TestCase):
    def test_default_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, r2.id - 1)

    def test_custom_id_assignement(self):
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

    def test_invalid_height_value(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as context:
            r.height = -2
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_invalid_width_value_zero(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(0, 10)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_invalid_height_value_zero(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 0)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError) as context:
            Rectangle("10", 2)
        self.assertEqual(str(context.exception), "width must be an integer")

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

    def test_invalid_x_value(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 2, -3, 1)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_invalid_y_type(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError) as context:
            r.y = {}
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_invalid_y_value(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_invalid_x_type_str(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, 2, "3")
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_invalid_y_type_str(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, 2, 4, "3")
        self.assertEqual(str(context.exception), "y must be an integer")

class TestRectangle_Area(unittest.TestCase):
    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

class TestRectangle_Height(unittest.TestCase):
    def test_height_str(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, "Holberton")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_float(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, 2.0)
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_tuple(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, (1, 2, 3))
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_list(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, [1, 2, 3])
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_set(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, {1, 2, 3})
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_dict(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, {"a": 0, "b": 1})
        self.assertEqual(str(context.exception), "height must be an integer")


class TestRectangle_Str(unittest.TestCase):
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "[Rectangle] (1) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1, id=2)
        captured_output = StringIO()
        sys.stdout = captured_output
        print(r2)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "[Rectangle] (2) 1/0 - 5/5")


class TestRectangle_Update(unittest.TestCase):
    def test_update_id(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_width(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_height(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_x(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_y(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")


class TestRectangle_To_Dictionary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.reset_nb_objects()

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        expected_dict = {'x': 1, 'y': 9, 'id': r1.id, 'height': 2, 'width': 10}
        self.assertEqual(r1_dict, expected_dict)

    def test_update_from_dictionary(self):
        r1 = Rectangle(1, 1)
        r1_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        r1.update(**r1_dict)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/9 - 10/2")

    def test_equality_after_update(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r1_dict = r1.to_dictionary()
        r2.update(**r1_dict)
        self.assertFalse(r1 == r2)


if __name__ == '__main__':
    unittest.main()
