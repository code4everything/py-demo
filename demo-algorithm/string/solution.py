# coding:utf-8

from collections import Counter


class Solution:
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
