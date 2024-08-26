# 538. 把二叉搜索树转换为累加树
# https://programmercarl.com/0538.%E6%8A%8A%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E8%BD%AC%E6%8D%A2%E4%B8%BA%E7%B4%AF%E5%8A%A0%E6%A0%91.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/convert-bst-to-greater-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.greater_sum = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # 中序遍历倒（左中右）过来遍历， 右中左。
        if root.right:
            root.right = self.convertBST(root.right)

        self.greater_sum += root.val
        root.val = self.greater_sum
        if root.left:
            root.left = self.convertBST(root.left)
        return root