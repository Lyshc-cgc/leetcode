# 968. 监控二叉树
# https://programmercarl.com/0968.%E7%9B%91%E6%8E%A7%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/binary-tree-cameras/description/

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def traversal(self, node,):
        if not node:  # 空节点，有覆盖
            return 2

        left = self.traversal(node.left)
        right = self.traversal(node.right)

        # 左右孩子都有覆盖，自己就无覆盖
        if left == 2 and right == 2:
            return 0

        # 左右孩子中有一个无覆盖，自己需要安摄像头
        if left == 0 or right == 0:
            self.res += 1
            return 1

        # 左右孩子中有一个有摄像头,自己就被覆盖了
        if left == 1 or right == 1:
            return 2

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if self.traversal(root) == 0:  # 判断根节点是否被覆盖
            self.res += 1
        return self.res
