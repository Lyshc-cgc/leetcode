# 404. 左叶子之和
# https://programmercarl.com/0404.%E5%B7%A6%E5%8F%B6%E5%AD%90%E4%B9%8B%E5%92%8C.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/sum-of-left-leaves/description/

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traversal(self, node: Optional[TreeNode], is_left, count):
        """

        :param node:
        :param is_left: 指示该节点是否为左节点
        :param count: 左叶子结点的和
        :return:
        """
        if not node:
            return
        if is_left and not node.left and not node.right:  # 左孩子节点
            count[0] += node.val
            return
        if node.left:
            self.traversal(node.left, True, count)
        if node.right:
            self.traversal(node.right, False, count)
        return


    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        count = [0]
        if not root:
            return count[0]
        if root and not root.left and not root.right:
            return count[0]
        self.traversal(root.left, True, count)
        self.traversal(root.right, False, count)
        return count[0]
