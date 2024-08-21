# 617. 合并二叉树
# https://programmercarl.com/0617.%E5%90%88%E5%B9%B6%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/merge-two-binary-trees/description/

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:  # 两个都为空，则返回
            return None
        # 至少有一个不为空
        left1, left2 = None, None
        right1, right2 = None, None
        v1, v2 = 0, 0
        if root1:
            v1 = root1.val
            left1 = root1.left
            right1 = root1.right
        if root2:
            v2 = root2.val
            left2 = root2.left
            right2 = root2.right
        node = TreeNode(v1 + v2)
        node.left = self.mergeTrees(left1, left2)
        node.right = self.mergeTrees(right1, right2)
        return node
