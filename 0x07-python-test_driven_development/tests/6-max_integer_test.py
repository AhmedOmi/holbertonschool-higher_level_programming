#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def max_integer(self):
        self.assertEqual('len(list) == 0'.max_integer(), 'None')


if __name__ == '__main__':
    unittest.main()
