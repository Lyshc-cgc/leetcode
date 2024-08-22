# 701. 二叉搜索树中的插入操作
# https://programmercarl.com/0701.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E6%8F%92%E5%85%A5%E6%93%8D%E4%BD%9C.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/insert-into-a-binary-search-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insert(self, node: Optional[TreeNode], val: int):
        if val < node.val and not node.left:
            node.left = TreeNode(val)
            return
        elif val > node.val and not node.right:
            node.right = TreeNode(val)
            return
        if val < node.val:  # 左孩子不空，往做孩子遍历，找插入位置
            self.insert(node.left, val)
        else:
            self.insert(node.right, val)

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        self.insert(root, val)
        return root
