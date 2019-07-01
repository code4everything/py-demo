# coding:utf-8

from list.tree_node import TreeNode


class Solution:

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        LeetCode(id=404,title=左叶子之和,difficulty=medium)
        """
        if root:
            val = 0
            if root.left and root.left.left is None and root.left.right is None:
                val = root.left.Val
            return val + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        return 0
