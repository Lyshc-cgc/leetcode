# 637. 二叉树的层平均值
# https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html#_637-%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%B9%B3%E5%9D%87%E5%80%BC
# https://leetcode.cn/problems/average-of-levels-in-binary-tree/description/

from typing import Optional, List
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    class Solution:
        def levelOrder(self, root: Node) -> List[List[int]]:
            res = []
            if not root:
                return res
            q = deque([root])
            while q:
                size = len(q)
                level = []
                for _ in range(size):
                    node = q.popleft()
                    level.append(node.val)
                    if node.children:
                        for e in node.children:
                            q.append(e)
                res.append(level)
            return res

