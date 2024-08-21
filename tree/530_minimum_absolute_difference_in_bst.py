# 530. 二叉搜索树的最小绝对差
# https://programmercarl.com/0530.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E7%BB%9D%E5%AF%B9%E5%B7%AE.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.min_div = float('inf')
        self.pre_val = -1

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return

        if root.left:
            self.getMinimumDifference(root.left)
        if self.pre_val != -1:  # 除开第一个叶子结点
            self.min_div = min(self.min_div, abs(self.pre_val - root.val))
        self.pre_val = root.val
        if root.right:
            self.getMinimumDifference(root.right)
        return self.min_div

