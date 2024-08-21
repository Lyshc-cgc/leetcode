# 98. 验证二叉搜索树
# https://programmercarl.com/0098.%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/validate-binary-search-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pre = float('-inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:  # 空树也是BST
            return True
        left_res = self.isValidBST(root.left)
        if root.val > self.pre:
            self.pre = root.val
        else:
            return False
        right_res = self.isValidBST(root.right)
        return left_res and right_res

