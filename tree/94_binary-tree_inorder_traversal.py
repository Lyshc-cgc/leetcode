# 94. 二叉树的中序遍历
# https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%80%92%E5%BD%92%E9%81%8D%E5%8E%86.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/binary-tree-inorder-traversal/description/
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traversal(self, root: Optional[TreeNode], res: List[int]):
        if not root:
            return
        self.traversal(root.left, res)
        res.append(root.val)
        self.traversal(root.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traversal(root, res)
        return res

    def in_iter(self, root: Optional[TreeNode]) -> List[int]:
        """
        中序，迭代法
        :param root:
        :return:
        """
        stack, res = [], []
        if not root:
            return res
        cur = root  # cur指向需要访问结点
        while cur or stack:
            if cur:  # 一直往左深入找到底
                stack.append(cur)
                cur = cur.left  # 左
            else:  # 指到底了，开始处理
                cur = stack.pop()  # 中
                res.append(cur.val)
                cur = cur.right  # 右
        return res

    def uni_inter(self, root: Optional[TreeNode]) -> List[int]:
        """
        统一风格迭代法
        :param root:
        :return:
        """
        stack = deque()
        res = []
        if not root:
            return res
        stack.append(root)
        while stack:
            top = stack.pop()
            if top:  # 若不为空，则继续遍历
                if top.right:
                    stack.append(top.right)
                stack.append(top)
                stack.append(None)
                if top.left:
                    stack.append(top.left)
            else:  # 若为空，则操作栈顶结点
                top = stack.pop()
                res.append(top.val)
        return res