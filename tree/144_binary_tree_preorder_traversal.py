# 144. 二叉树的前序遍历
# https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%80%92%E5%BD%92%E9%81%8D%E5%8E%86.html#%E6%80%9D%E8%B7%AF
# https://leetcode.cn/problems/binary-tree-preorder-traversal/description/

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traversal(self, root: Optional[TreeNode], res: List[int]):
        if not root:
            return
        res.append(root.val)
        self.traversal(root.left, res)
        self.traversal(root.right, res)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traversal(root, res)
        return res

    def pre_iter(self, root: Optional[TreeNode]) -> List[int]:
        """
        前序，迭代法
        :param root:
        :return:
        """
        stack = []
        res = []
        if not root:
            return res
        stack.append(root)
        while stack:
            p = stack.pop()
            res.append(p.val)
            if p.right:  # 右孩子先入栈，后出栈处理
                stack.append(p.right)
            if p.left:  # 左孩子后入栈，先出栈处理
                stack.append(p.left)
        return res


if __name__ == '__main__':

    pass
