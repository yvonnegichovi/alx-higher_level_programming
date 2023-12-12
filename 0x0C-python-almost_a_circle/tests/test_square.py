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

    def test_invalid_size_type_list(self):
        with self.assertRaises(TypeError) as context:
            Square([1, 2, 3])
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_invalid_size_type_set(self):
        with self.assertRaises(TypeError) as context:
            Square({1, 2, 3})
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_invalid_size_type_dict(self):
        with self.assertRaises(TypeError) as context:
            Square({"a": 0, "b": 1})
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_invalid_width_value_square(self):
        with self.assertRaises(ValueError) as context:
            s = Square(-10)
        self.assertEqual(str(context.exception), "width must be > 0")


class TestSquare_Str(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.reset_nb_objects() 

    def test_square_str(self):
        s1 = Square(3, 1, 3)
        captured_output = StringIO()
        sys.stdout = captured_output
        print(s1)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "[Square] (1) 1/3 - 3")


class TestSquare_update(unittest.TestCase):
    def test_update_square_id(self):
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

    def test_update_square_size(self):
        s1 = Square(5)
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

    def test_update_square_x(self):
        s1 = Square(5)
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

    def test_update_square_y(self):
        s1 = Square(5)
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")


class TestSquare_To_Dictionary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.reset_nb_objects()

    def test_to_dictionary_square(self):
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        expected_dict = {'id': s1.id, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dict, expected_dict)

    def test_update_from_dictionary_square(self):
        s1 = Square(1, 1)
        s1_dict = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        s1.update(**s1_dict)
        self.assertEqual(str(s1), "[Square] (1) 2/1 - 10")

    def test_equality_after_update_square(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s1_dict = s1.to_dictionary()
        s2.update(**s1_dict)
        self.assertFalse(s1 == s2)


if __name__ == '__main__':
    unittest.main()
