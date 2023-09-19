#!/usr/bin/python3
"""test the functionality of the code"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """contains attributes, instances and methods to be tested"""
    def test_bases(self):
        """Tests for id processes"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    """Test different id values"""
    def test_diff_id(self):
        """Accept different id values"""
        self.assertEqual(12, Base(12).id)
        b5 = Base()
        self.assertEqual(b5.id, 4)

"""class to test json string method"""
class test_json_string(unittest.TestCase):
    """tests the string method of json"""
    def test_str_json(self):
        """tests for correct output"""
        r1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(str, type(Base.to_json_string([r1.to_dictionary()])))

"""class to test the save_to_file function"""
class test_save(unittest.TestCase):
    """tests whether the function save_to_file works well"""
    def test_save_file(self):
        """test the loads function"""
        r1 = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    """tests two rectangles"""
    def test_two_save(self):
        """tests the save function with two rectangles"""
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

if __name__ == '__main__':
    unittest.main()
