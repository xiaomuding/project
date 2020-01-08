# -*- coding: utf-8 -*-

import unittest
from old.mathfunc import *


class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    @classmethod
    def setUpClass(cls):
        print ("This setUpClass() method only called once.\n")

    @classmethod
    def tearDownClass(cls):
        print ("This tearDownClass() method only called once too.")

    @unittest.skip("I don't want to run this case.")
    def test_add(self):
        print("test 2")
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        print("test 3")
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        print("test 4")
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        print("test 5")
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(divide(5, 2), 2.5)

