# coding:utf-8


class Solution:
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

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
