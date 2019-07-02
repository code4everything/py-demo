# coding:utf-8

import unittest

from maths.solution import Solution


class TestMath(unittest.TestCase):
    s = Solution()

    def test_arrange_coins(self):
        self.assertEqual(self.s.arrangeCoins(1), 1)
        self.assertEqual(self.s.arrangeCoins(5), 2)
        self.assertEqual(self.s.arrangeCoins(8), 3)
        self.assertEqual(self.s.arrangeCoins(10), 4)
        self.assertEqual(self.s.arrangeCoins(17), 5)

    def test_third_max(self):
        self.assertEqual(self.s.thirdMax([3, 2, 1]), 1)
        self.assertEqual(self.s.thirdMax([1, 2]), 2)
        self.assertEqual(self.s.thirdMax([2, 2, 3, 1]), 1)
        self.assertEqual(self.s.thirdMax([3, 2, 1, 3, 5, 6, 4, 5, 6, 7, 5, 4, 5, 6, 6, 5]), 5)

    def test_to_hex(self):
        self.assertEqual(self.s.toHex(26), '1a')
        self.assertEqual(self.s.toHex(-1), 'ffffffff')
        self.assertEqual(self.s.toHex(-2), 'fffffffe')
        self.assertEqual(self.s.toHex(-16), 'fffffff0')
