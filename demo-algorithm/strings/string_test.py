# coding:utf-8

import unittest

from strings.solution import Solution


class TestString(unittest.TestCase):
    s = Solution()

    def test_compress(self):
        self.s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])

    def test_find_anagrams(self):
        self.s.findAnagrams("cbaebabacd", "abc")
