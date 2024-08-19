# 637. 二叉树的层平均值
# https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html#_637-%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%B9%B3%E5%9D%87%E5%80%BC
# https://leetcode.cn/problems/average-of-levels-in-binary-tree/description/

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        avgs = []
        if not root:
            return avgs
        q = deque([root])
        while q:
            size = len(q)
            avg = []
            for _ in range(size):
                node = q.popleft()
                avg.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            avgs.append(sum(avg) / size)
        return avgs

