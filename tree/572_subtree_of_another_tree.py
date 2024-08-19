# 572. 另一棵树的子树
# https://leetcode.cn/problems/subtree-of-another-tree/description/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        判断p,q两棵树是否相同
        :param p:
        :param q:
        :return:
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        # 两者都不为空，且值相等.再分别判断左右孩子
        return self.is_same(p.left, q.left) and self.is_same(p.right, q.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        flag = self.is_same(root, subRoot)  # 先判断root所在树和subroot是否相同
        if flag:
            return True
        else:  # 再分别判断左右子树
            if root.left and self.isSubtree(root.left, subRoot):
                return True
            if root.right and self.isSubtree(root.right, subRoot):
                return True
        return False
