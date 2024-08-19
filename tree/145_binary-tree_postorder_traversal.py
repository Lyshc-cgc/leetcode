# 145. 二叉树的后序遍历
# https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%80%92%E5%BD%92%E9%81%8D%E5%8E%86.html#%E6%80%9D%E8%B7%AF
# https://leetcode.cn/problems/binary-tree-postorder-traversal/description/
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traversal(root, res)
        return res

    def traversal(self, root: Optional[TreeNode], res: List):
        if not root:
            return
        self.traversal(root.left, res)
        self.traversal(root.right, res)
        res.append(root.val)

    def post_inter(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [], []
        if not root:
            return res
        stack.append(root)
        while stack:
            p = stack.pop()  # 中
            res.append(p.val)
            if p.left:  # 左孩子先入栈，后处理
                stack.append(p.left)
            if p.right:  # 右孩子，先处理
                stack.append(p.right)
        return res[::-1]

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
                stack.append(top)
                stack.append(None)
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)
            else:  # 若为空，则操作栈顶结点
                top = stack.pop()
                res.append(top.val)
        return res


