#!/usr/bin/python3

"""Unittest for base.py
Unittest classes:
    TestBase_Constructor - line 14
    """

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_Constructor(unittest.TestCase):
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


class TestBase_ToJsonString(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.reset_nb_objects()

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        expected_json_string = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]'
        self.assertEqual(json_string, expected_json_string)

    def test_to_json_string_empty_list(self):
        json_string = Base.to_json_string([])
        expected_json_string = "[]"
        self.assertEqual(json_string, expected_json_string)

    def test_to_json_string_none_list(self):
        json_string = Base.to_json_string(None)
        expected_json_string = "[]"
        self.assertEqual(json_string, expected_json_string)


class TestRectangle_Create_Method(unittest.TestCase):
    def test_create_method(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)


class TestRectangle_Save_to_File(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.reset_nb_objects()

    def test_save_to_file_method(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            file_content = file.read()
        self.assertEqual(file_content, '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, {"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]')


if __name__ == '__main__':
    unittest.main()
