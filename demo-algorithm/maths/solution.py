# coding:utf-8
from typing import List


class Solution:
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        LeetCode(id=463,title=岛屿的周长,difficulty=easy)
        """
        length = len(grid)
        width = len(grid[0])
        prm = 0
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    if j == 0 or grid[i][j - 1] == 0:
                        prm += 1
                    if i == 0 or grid[i - 1][j] == 0:
                        prm += 1
        return prm * 2

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        LeetCode(id=455,title=分发饼干,difficulty=easy)
        """
        g.sort()
        s.sort()
        gi, si, res = 0, 0, 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                gi += 1
                res += 1
            si += 1
        return res

    def minMoves(self, nums: List[int]) -> int:
        """
        LeetCode(id=453,title=最小移动次数使数组元素相等,difficulty=easy)
        """
        return sum(nums) - min(nums) * len(nums)

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        LeetCode(id=448,title=找到所有数组中消失的数字,difficulty=easy)
        """
        size = len(nums)
        tmp = [0 for i in range(0, size)]
        while size > 0:
            size -= 1
            tmp[nums[size] - 1] += 1
        res = []
        idx = 0
        for n in tmp:
            idx += 1
            if n == 0:
                res.append(idx)
        return res

    def arrangeCoins(self, n: int) -> int:
        """
        LeetCode(id=441,title=排列硬币,difficulty=easy)
        """
        left, right = 0, n + 1
        while left < right:
            mid = left + ((right - left) >> 1)
            if (((1 + mid) * mid) >> 1) <= n:
                left = mid + 1
            else:
                right = mid
        return right - 1

    def thirdMax(self, nums: List[int]) -> int:
        """
        LeetCode(id=414,title=第三大的数,difficulty=easy)
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
        LeetCode(id=405,title=数字转换为十六进制数,difficulty=easy)
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
