# coding:utf-8

import unittest

from strings.solution import Solution


class TestString(unittest.TestCase):
    s = Solution()

    def test_find_anagrams(self):
        self.s.findAnagrams("cbaebabacd", "abc")
