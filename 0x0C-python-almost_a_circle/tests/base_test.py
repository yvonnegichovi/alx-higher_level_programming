#!/usr/bin/python3

"""Unittest for class Base"""


import unittest
from models.base import Base


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
