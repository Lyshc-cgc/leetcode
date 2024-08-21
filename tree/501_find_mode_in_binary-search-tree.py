# 501. 二叉搜索树中的众数
# https://programmercarl.com/0501.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E4%BC%97%E6%95%B0.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/find-mode-in-binary-search-tree/description/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        self.modes = dict()

    def traversal(self, node: Optional[TreeNode]):
        if not node:
            return
        self.traversal(node.left)
        self.modes[node.val] = self.modes.get(node.val, 0) + 1
        self.traversal(node.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal(root)
        self.modes = sorted(self.modes.items(), key=lambda x: x[1], reverse=True)  # 降序
        max_count = 0
        res = []
        for idx, (num, count) in enumerate(self.modes):
            if idx == 0:
                max_count = count
            if count == max_count:
                res.append(num)
        return res
