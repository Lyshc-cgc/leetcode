# 669. 修剪二叉搜索树
# https://programmercarl.com/0669.%E4%BF%AE%E5%89%AA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/trim-a-binary-search-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.left:
            root.left = self.trimBST(root.left, low, high)
        if root.right:
            root.right = self.trimBST(root.right, low, high)

        if root.val < low or root.val > high:
            if not root.left and not root.right:
                return None
            elif not root.left and root.right:
                return root.right
            elif root.left and not root.right:  # 这里估计不会走
                return root.left
            else:  # 直接让右节点顶上，因为此时root和左节点均小于Low
                return root.right

        return root
