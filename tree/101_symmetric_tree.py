# 101. 对称二叉树
# https://programmercarl.com/0101.%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/symmetric-tree/description/

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root.left, root.right])
        while q:
            left, right = q.popleft(), q.popleft()
            # 先看两者是否均为空，均为空（可以视作镜像），则跳过此次遍历
            if not left and not right:
                continue

            # 走到这里，说明left和right中至少有一个不为空
            if not left or not right or left.val != right.val:
                return False

            # 到这里说明，两者不为空且值相等
            # 外侧
            q.append(left.left)
            q.append(right.right)
            # 内侧
            q.append(left.right)
            q.append(right.left)
        return True
