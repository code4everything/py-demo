# coding:utf-8
from typing import List


class Solution:
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    def thirdMax(self, nums: List[int]) -> int:
        """
        LeetCode(id=414,title=第三大的数,difficulty=ease)
        """
        maxs = []
        for n in nums:
            i = 0
            t = n
            while i < 3:
                if i < len(maxs):
                    if t == maxs[i]:
                        break
                    elif t > maxs[i]:
                        maxs[i], t = t, maxs[i]
                else:
                    maxs.append(t)
                    break
                i = i + 1
        if len(maxs) == 3:
            return maxs[2]
        return maxs[0]

    def toHex(self, num: int) -> str:
        """
        LeetCode(id=405,title=数字转换为十六进制数,difficulty=ease)
        """
        negative = num < 0
        if negative:
            num = -num
        res = []
        while num > 15:
            res.append(num & 15)
            num = num >> 4
        res.append(num)
        if negative:
            i = 0
            while i < 8:
                if i < len(res):
                    res[i] = 15 - res[i]
                else:
                    res.append(15)
                i = i + 1
            i = 0
            base = 1
            while base > 0:
                n = res[i] + base
                if n == 16:
                    res[i] = 0
                    i = i + 1
                else:
                    res[i] = n
                    base = 0
        i = len(res) - 1
        s = ''
        while i > -1:
            s = s + self.hex[res[i]]
            i = i - 1
        return s
