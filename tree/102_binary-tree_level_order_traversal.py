# 102. 二叉树的层序遍历
# https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html#_102-%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86
# https://leetcode.cn/problems/binary-tree-level-order-traversal/description/

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        all_res = []
        q = deque()
        if not root:
            return all_res
        q.append(root)
        while q:
            res_level = []
            size = len(q)
            while size:
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                res_level.append(node.val)
                size -= 1
            all_res.append(res_level)
        return all_res
