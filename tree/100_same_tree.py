# 100. 相同的树
# https://leetcode.cn/problems/same-tree/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  # 都为空，相同
            return True
        if not p or not q or p.val != q.val:  # 有一个为空，或两者不相等
            return False

        # 此时是两者均不为空，且值相等的情况
        # 继续遍历
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

