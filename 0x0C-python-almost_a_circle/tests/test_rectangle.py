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

if __name__ == '__main__':
    unittest.main()
