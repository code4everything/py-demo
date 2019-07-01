# coding:utf-8

import unittest

from maths.solution import Solution


class TestMath(unittest.TestCase):
    s = Solution()

    def test_to_hex(self):
        self.assertEqual(self.s.toHex(26), '1a')
        self.assertEqual(self.s.toHex(-1), 'ffffffff')
        self.assertEqual(self.s.toHex(-2), 'fffffffe')
        self.assertEqual(self.s.toHex(-16), 'fffffff0')
