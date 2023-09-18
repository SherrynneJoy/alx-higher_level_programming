import unittest
import io
import sys
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class test_square(unittest.TestCase):
    """tests the methods and attributes of class square"""
    def test_area(self):
        """tests if the area function works well"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

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
        s1 = Square(5)
        capture = Test_stdout.capture_stdout(s1, "display")
        self.assertEqual("#####\n#####\n#####\n#####\n#####\n", capture.getvalue())
        s2 = Square(2, 2)
        capture = Test_stdout.capture_stdout(s2, "display")
        self.assertEqual("  ##\n  ##\n", capture.getvalue())

    """Test display with 4 args"""
    def test_display_four(self):
        """accepts four arguments"""
        s1 = Square(3, 1, 3)
        capture = Test_stdout.capture_stdout(s1, "display")
        self.assertEqual("\n\n\n ###\n ###\n ###\n", capture.getvalue())

    """Tests the __str__ method"""
    def test_str(self):
        """Tests whether the str methods prints to stdout"""
        s1 = Square(5)
        capture = Test_stdout.capture_stdout(s1, "print")
        correct = "[Square] (27) 0/0 - 5\n".format(s1.id)
        self.assertEqual(correct, capture.getvalue())
        s2 = Square(2, 2)
        capture = Test_stdout.capture_stdout(s2, "print")
        correct = "[Square] (28) 2/0 - 2\n".format(s2.id)
        self.assertEqual(correct, capture.getvalue())
        s3 = Square(3, 1, 3)
        capture = Test_stdout.capture_stdout(s3, "print")
        correct = "[Square] (29) 1/3 - 3\n".format(s3.id)
        self.assertEqual(correct, capture.getvalue())

    """A function to raise errors"""
    def test_errors(self):
        """tests whether the errors are raised appropriately"""
        self.assertRaises(Exception)

    """Tests the update function"""
    def test_update(self):
        """tests the functionality of the update function"""
        s1 = Square(5)
        capture = Test_stdout.capture_stdout(s1, "print")
        correct = "[Square] (30) 0/0 - 5\n".format(s1.id)
        self.assertEqual(correct, capture.getvalue())
        s1.update(10)
        self.assertEqual("[Square] (10) 0/0 - 5", str(s1))
        s1.update(1, 2)
        self.assertEqual("[Square] (1) 0/0 - 2", str(s1))
        s1.update(1, 2, 3)
        self.assertEqual("[Square] (1) 3/0 - 2", str(s1))
        s1.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/0 - 2", str(s1))

    """tests the kwargs"""
    def test_kwargs(self):
        """tests whether the kwargs works appropriately"""
        s1 = Square(5)
        capture = Test_stdout.capture_stdout(s1, "print")
        correct = "[Square] (1) 0/0 - 5\n".format(s1.id)
        s1.update(x=12)
        self.assertEqual("[Square] (26) 12/0 - 5", str(s1))
        s1.update(size=7, y=1)
        self.assertEqual("[Square] (26) 12/0 - 7", str(s1))
        s1.update(size=7, id=89, y=1)
        self.assertEqual("[Square] (89) 12/0 - 7", str(s1))

if __name__ == '__main__':
    unittest.main()
