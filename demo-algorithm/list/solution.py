# coding:utf-8

from list.tree_node import TreeNode


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:
        """
        LeetCode(id=437,title=路径总和 III,difficulty=easy)
        """
        if not root:
            return 0

        def dfs(root, sum):
            count = 0  # 记录路径个数
            if not root:
                return 0
            if root.val == sum:
                count += 1
            count += dfs(root.left, sum - root.val)
            count += dfs(root.right, sum - root.val)
            return count

        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        LeetCode(id=404,title=左叶子之和,difficulty=easy)
        """
        if root:
            val = 0
            if root.left and root.left.left is None and root.left.right is None:
                val = root.left.Val
            return val + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        return 0
