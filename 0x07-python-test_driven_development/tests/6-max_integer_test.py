#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_case(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_all_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
