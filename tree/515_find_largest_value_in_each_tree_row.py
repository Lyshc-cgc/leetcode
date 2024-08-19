# 515. 在每个树行中找最大值
# https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html#_515-%E5%9C%A8%E6%AF%8F%E4%B8%AA%E6%A0%91%E8%A1%8C%E4%B8%AD%E6%89%BE%E6%9C%80%E5%A4%A7%E5%80%BC
# https://leetcode.cn/problems/find-largest-value-in-each-tree-row/description/

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            size = len(q)
            max_val = float('-inf')
            for _ in range(size):
                node = q.popleft()
                max_val = max(max_val, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(max_val)
        return res

