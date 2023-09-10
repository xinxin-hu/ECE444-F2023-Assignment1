import unittest

from utils import reversed
from utils import formatter

class MyTestCase(unittest.TestCase):
    def test_revered(self):
        case_str = "1234"
        case_floats = 123.4
        case_int = 1234
        reversed_int = reversed(case_int)
        reversed_str = reversed(case_str)
        reversed_floats = reversed(case_floats)

        self.assertEqual(reversed_int, 4321)  # add assertion here
        self.assertEqual(reversed_str, 0)
        self.assertEqual(reversed_floats,0)
    def test_formatter(self):
        case_str = "13"
        case_floats = 1.3
        case_int = 13
        list_int = formatter(case_int)
        list_floats = formatter(case_floats)
        list_str = formatter(case_str)

        self.assertEqual(list_int[0], bin(13))  # add assertion here
        self.assertEqual(list_int[1],oct(13))
        self.assertEqual(len(list_floats),0)
        self.assertEqual(len(list_str), 0)

if __name__ == '__main__':
    print("this program consists unit tests")
    unittest.main()
    print("this program passes all tests")
