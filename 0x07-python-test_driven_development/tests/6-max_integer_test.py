#!/usr/bin/python3
"""Unittest module."""


import unittest, sys
sys.path.append('../')

max_integer = __import__('6-max_integer').max_integer

class TextMaxInteger(unittest.TestCase):
    """Test Class module."""

    def setUp(self):
        self.sorted_list = max_integer([1, 2, 3, 4])
        self.unsorted_list = max_integer([1, 3, 4, 2])
        self.empty_list = max_integer()
        self.float_list = max_integer([9.1, 10.2, 9.8])
        self.int_float_list = max_integer([10.1, 11, 11.1])
        self.single_list = max_integer([12])
        self.str_list = max_integer(["abc", "edf", "zig"])
        self.one_string = max_integer("cpython")
        self.empty_string = max_integer("")

    def test_sorted_list(self):
        """Inside test_sorted_list method."""
        self.assertEqual(self.sorted_list, 4)

    def test_unsorted_list(self):
        """Inside test_unsorted_list method."""
        self.assertEqual(self.unsorted_list, 4)

    def test_empty_list(self):
        """Inside test_empty_list method."""
        self.assertEqual(self.empty_list, None)

    def test_float_list(self):
        """Inside test_float_list method."""
        self.assertEqual(self.float_list, 10.2)

    def test_int_and_float_list(self):
        """Inside int and float list method."""
        self.assertEqual(self.int_float_list, 11.1)

    def test_single_list(self):
        """Inside single list method."""
        self.assertEqual(self.single_list, 12)

    def test_str_list(self):
        """Inside str list method."""
        self.assertEqual(self.str_list, "zig")

    def test_one_string(self):
        """Inse one_string method."""
        self.assertEqual(self.one_string, "y")

    def test_empty_string(self):
        """Inside empty str method."""
        self.assertEqual(self.empty_string, None)

if __name__ == '__main__':
    unittest.main()
