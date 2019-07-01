# coding:utf-8
from collections import Counter, deque


class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        """
        LeetCode(id=415,title=字符串相加,difficulty=medium)
        """
        len1 = len(num1)
        len2 = len(num2)
        size = max(len1, len2)
        base = 0
        q = deque()
        for i in range(0, size):
            n = base
            if i < len1:
                n += int(num1[len1 - i - 1])
            if i < len(num2):
                n += int(num2[len2 - i - 1])
            if n > 9:
                base = 1
                q.insert(0, str(n - 10))
            else:
                base = 0
                q.insert(0, str(n))
        if base == 1:
            return "1".join(q)
        return "".join(q)

    def longestPalindrome(self, s: str) -> int:
        """
        LeetCode(id=409,title=最长回文串,difficulty=medium)
        """
        m = {}
        for c in s:
            m[c] = m.get(c, 0) + 1
        size = 0
        add = False
        for v in m.values():
            if v & 1 == 1:
                add = True
                size = size + v - 1
            else:
                size = size + v
        if add:
            size = size + 1
        return size

    def frequency_sort(self, s: str) -> str:
        """
        LeetCode(id=451,title=根据字符出现频率排序,difficulty=medium)
        """
        lens = len(s)
        sc = dict(Counter(s))
        ll = ['' for i in range(0, lens + 1)]
        ret = ""
        for k, v in sc.items():
            ll[v] += k * v
        for i in range(lens, -1, -1):
            if ll[i] != '':
                ret += ll[i]
        return ret
