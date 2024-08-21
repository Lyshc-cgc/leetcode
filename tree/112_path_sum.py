# 112. 路径总和
# https://programmercarl.com/0112.%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/path-sum/description/

from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traversal(self, node: Optional[TreeNode], path: List[int], target: int) -> bool:
        if not node.left and not node.right:  # 叶子结点
            return target == sum(path) + node.val
        if node:
            path.append(node.val)
            l_flag, r_flag = False, False
            if node.left:
                l_flag = self.traversal(node.left, path, target)
            if node.right:
                r_flag = self.traversal(node.right, path, target)
            path.pop()  # 回溯， 弹出最后本节点值
            return l_flag or r_flag   # 有一个满足即可


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        path = []
        return self.traversal(root, path, targetSum)