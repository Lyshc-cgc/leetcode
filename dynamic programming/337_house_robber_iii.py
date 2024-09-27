# 337. 打家劫舍 III
# https://programmercarl.com/0337.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DIII.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/house-robber-iii/description/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traversal(self, node):
        if not node:
            return 0, 0  # 0位置是不偷该房间的最大的价值，1位置是偷..

        # 后序遍历
        left_vals = self.traversal(node.left)
        right_vals = self.traversal(node.right)

        # 0位置是不偷该房间能偷的最大价值。此时左右孩子都可以偷。
        # 对于左孩子,max(left_vals[0], left_vals[1])，选择偷还是不偷价值不一样，取最大的
        # 右孩子同理
        # 1位置是偷..
        return max(left_vals[0], left_vals[1]) + max(right_vals[0], right_vals[1]), node.val + left_vals[0] + right_vals[0]

    def rob(self, root: Optional[TreeNode]) -> int:

        left, right = self.traversal(root)
        return max(left, right)


