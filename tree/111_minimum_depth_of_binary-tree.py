# 111. 二叉树的最小深度
# https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html#_111-%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E6%B7%B1%E5%BA%A6
# https://leetcode.cn/problems/minimum-depth-of-binary-tree/description/

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        height = 0
        if not root:
            return height
        q = deque([root])
        while q:
            size = len(q)
            height += 1
            for _ in range(size):
                node = q.popleft()
                if not node.left and not node.right:  # 找到第一个叶子结点，直接返回高度
                    return height
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)