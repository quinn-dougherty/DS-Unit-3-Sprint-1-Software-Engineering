#!/usr/bin/env python

import unittest
from scratch import *

# newton_sqrt1, newton_sqrt2, lazy_sqrt, builtin_sqrt


class SqrtTests(unittest.TestCase):
    """Obligatory docstring, test square roots!"""
    def test_sqrt9(self):
        self.assertEqual(newton_sqrt1(9), 3)

    def test_sqrt2(self):
        self.assertAlmostEqual(newton_sqrt1(2), 1.41421356237)


class SquaringTests(unittest.TestCase):
    def test_thing(self):
        pass


if __name__ == '__main__':
    unittest.main()
