import unittest
import io
import sys
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

"""Class to test stdout"""


class Test_stdout(unittest.TestCase):
    """Test if text is printed to stdout"""

    @staticmethod
    def capture_stdout(rect, method):
        """tests the stdout function"""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return (capture)

    """Test the display method"""
    def test_display(self):
        """tests whether display prints to stdout"""
        r1 = Rectangle(4, 6)
        capture = Test_stdout.capture_stdout(r1, "display")
        self.assertEqual("####\n####\n####\n####\n####\n####\n", capture.getvalue())
        r2 = Rectangle(2, 2)
        capture = Test_stdout.capture_stdout(r2, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    """Tests the __str__ method"""
    def test_str(self):
        """Tests whether the str methods prints to stdout"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        capture = Test_stdout.capture_stdout(r1, "print")
        correct = "[Rectangle] (12) 2/1 - 4/6\n".format(r1.id)
        self.assertEqual(correct, capture.getvalue())
        r2 = Rectangle(5, 5, 1)
        capture = Test_stdout.capture_stdout(r2, "print")
        correct = "[Rectangle] (13) 1/0 - 5/5\n".format(r2.id)
        self.assertEqual(correct, capture.getvalue())

if __name__ == '__main__':
    unittest.main()
