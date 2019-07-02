# coding:utf-8

from collections import Counter, deque
from typing import List


class Solution:

    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        LeetCode(id=459,title=重复的子字符串,difficulty=medium)
        """
        return (s + s)[1:-1].count(s) != 0

    def compress(self, chars: List[str]) -> int:
        """
        LeetCode(id=443,title=压缩字符串,difficulty=medium)
        """
        base = 0
        char = ''
        idx = 0
        for c in chars:
            if c != char:
                idx += self.lengthHelper(base, chars, idx)
                chars[idx] = c
                idx += 1
                base = 1
            else:
                base += 1
            char = c
        return idx + self.lengthHelper(base, chars, idx)

    def lengthHelper(self, n: int, chars: List[str], idx: int) -> int:
        if n < 2:
            return 0
        size = 1
        s = str(n)
        while n > 9:
            size += 1
            n /= 10
        for c in s:
            chars[idx] = c
            idx += 1
        return size

    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        LeetCode(id=438,title=找到字符串中所有字母异位词,difficulty=medium)
        """
        b = ord('a')
        result = []
        ps = [0 for i in range(0, 26)]
        for c in p:
            ps[ord(c) - b] += 1
        ss = [0 for i in range(0, 26)]
        start, end = 0, 0
        while end < len(s):
            n = ord(s[end]) - b
            end += 1
            ss[n] += 1
            while ss[n] > ps[n]:
                ss[ord(s[start]) - b] -= 1
                start += 1
            if end - start == len(p):
                result.append(start)
        return result

    def countSegments(self, s: str) -> int:
        """
        LeetCode(id=434,title=字符串中的单词数,difficulty=medium)
        """
        res = 0
        last = ' '
        for i in s:
            if i != ' ' and last == ' ':
                res += 1
            last = i
        return res

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
