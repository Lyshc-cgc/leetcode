# 513. 找树左下角的值
# https://programmercarl.com/0513.%E6%89%BE%E6%A0%91%E5%B7%A6%E4%B8%8B%E8%A7%92%E7%9A%84%E5%80%BC.html
# https://leetcode.cn/problems/find-bottom-left-tree-value/description/

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = []
        q = deque([root])
        while q:
            size = len(q)
            for idx in range(size):
                node = q.popleft()
                if idx == 0:  # 最左边的结点
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res[-1]  # 最后一个即为最底层的最左结点

