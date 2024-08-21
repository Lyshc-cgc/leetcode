# 113. 路径总和 II
# https://programmercarl.com/0112.%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/path-sum-ii/description/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traversal(self, node: Optional[TreeNode], path: List[int], res: List[List[int]], target: int):
        if not node:
            return
        if not node.right and not node.left:  # 叶子结点
            if target == sum(path) + node.val:
                tmp_res = [e for e in path]
                tmp_res.append(node.val)
                res.append(tmp_res)
            return
        path.append(node.val)
        self.traversal(node.left, path, res, target)
        self.traversal(node.right, path, res, target)
        path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        path = []
        self.traversal(root, path, res, targetSum)
        return res