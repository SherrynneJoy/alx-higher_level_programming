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

    """Test display with 4 args"""
    def test_display_four(self):
        """accepts four arguments"""
        r1 = Rectangle(2, 3, 2, 2)
        capture = Test_stdout.capture_stdout(r1, "display")
        self.assertEqual("\n\n  ##\n  ##\n  ##\n", capture.getvalue())

    """Tests the __str__ method"""
    def test_str(self):
        """Tests whether the str methods prints to stdout"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        capture = Test_stdout.capture_stdout(r1, "print")
        correct = "[Rectangle] (12) 2/1 - 4/6\n".format(r1.id)
        self.assertEqual(correct, capture.getvalue())
        r2 = Rectangle(5, 5, 1)
        capture = Test_stdout.capture_stdout(r2, "print")
        correct = "[Rectangle] (16) 1/0 - 5/5\n".format(r2.id)
        self.assertEqual(correct, capture.getvalue())
        r1 = Rectangle(10, 2, 1, 9)
        capture = Test_stdout.capture_stdout(r1, "print")
        correct = "[Rectangle] (17) 1/9 - 10/2\n".format(r1.id)
        self.assertEqual(correct, capture.getvalue())

    """Tests the update function"""
    def test_update(self):
        """tests the functionality of the update function"""
        r1 = Rectangle(10, 10, 10, 10)
        capture = Test_stdout.capture_stdout(r1, "print")
        correct = "[Rectangle] (18) 10/10 - 10/10\n".format(r1.id)
        self.assertEqual(correct, capture.getvalue())
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r1))
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r1))
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r1))
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r1))
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r1))

    """tests the kwargs"""
    def test_kwargs(self):
        """tests whether the kwargs works appropriately"""
        r1 = Rectangle(10, 10, 10, 10)
        capture = Test_stdout.capture_stdout(r1, "print")
        correct = "[Rectangle] (19) 10/10 - 10/10".format(r1.id)
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual("[Rectangle] (15) 10/10 - 10/1", str(r1))
        r1.update(width=1, x=2)
        self.assertEqual("[Rectangle] (15) 2/10 - 1/1", str(r1))
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual("[Rectangle] (89) 3/1 - 2/1", str(r1))
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r1))

"""a class to test the dictionary"""


class test_dict(unittest.TestCase):
    """tests whether the public method to_dictionary works"""
    def test_to_dictionary(self):
        """tests the dictionary method"""
        r1 = Rectangle(10, 2, 1, 9)
        correct = {'x': 1, 'y': 9, 'id': 27, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r1.to_dictionary())

    """comparing two dictionaries"""
    def test_compare_dict(self):
        """compares r1 and r2"""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    """tests whether the to_dictionary accepts the right argument"""
    def test_right_args(self):
        """tests whether the funciton returns the correct output"""
        r = Rectangle(4, 5, 6, 7)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == '__main__':
    unittest.main()
