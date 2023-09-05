#!/usr/bin/python3
#6-max_integer_test.py
"""Unittests for max_integer([...])."""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for function max_integer([...])"""
    def test_ordered_list(self):
        """Tests an ordered list of integers"""
        ordered_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered_list), 4)

    def test_unordered_list(self):
        """Tests an unordered list of inetegrs"""
        unordered_list = [1, 3, 2, 4]
        self.assertEqual(max_integer(unordered_list), 4)

    def test_max_at_start(self):
        """Tests a list where the largest number is at the start"""
        max_at_start = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_start), 4)

    def test_empty_list(self):
        """Checks for the largest integer in an empty list"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_element_list(self):
        """Tests for max integer in a single element list."""
        one_element = [12]
        self.assertEqual(max_integer(one_element), 12)

    def test_float_list(self):
        """Tests for max intger in a list containing floats"""
        float_list = [2.0, 10.1, 5.5]
        self.assertEqual(max_integer(float_integer), 10.1)

if __name__ == '__main__':
    unittest.main()
