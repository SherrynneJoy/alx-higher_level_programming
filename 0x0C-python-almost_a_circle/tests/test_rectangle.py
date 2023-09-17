import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Tests the methods and attributes in class Rectangle"""
    def test_rect_is_base(self):
        """tests if rectangle is an instance of base"""
        r1 = Rectangle(10, 2)
        self.assertIsInstance(Rectangle(10, 2), Base)
        r2 = Rectangle(2, 10)
        self.assertIsInstance(Rectangle(2, 10), Base)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertIsInstance(Rectangle(10, 2, 0, 0, 12), Base)

    """A function to raise errors"""
    def test_errors(self):
        """tests whether the errors are raised appropriately"""
        self.assertRaises(Exception)

    """A function to test the area"""
    def test_area(self):
        """tests if the area function works well"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

if __name__ == '__main__':
    unittest.main()
