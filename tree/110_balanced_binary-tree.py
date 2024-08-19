# 110. 平衡二叉树
# https://programmercarl.com/0110.%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/balanced-binary-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def get_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left_h = self.get_height(node.left)
        if left_h == -1:  # 不平衡
            return -1
        right_h = self.get_height(node.right)
        if right_h == -1:
            return -1

        if abs(left_h - right_h) > 1:
            return -1
        else:
            return 1 + max(left_h, right_h)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.get_height(root) == -1:
            return False
        else:
            return True