#!/usr/bin/python3
"""test the functionality of the code"""
import unittest
from models.base import Base


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

if __name__ == '__main__':
    unittest.main()
