# 236. 二叉树的最近公共祖先
# https://programmercarl.com/0236.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.path_p = None
        self.path_q = None
    def traversal(self, node: TreeNode, p: TreeNode, q: TreeNode, path: List[TreeNode]):

        if not node:
            return # 没找到
        path.append(node)
        if node.val == p.val:  # 记录p的路径
            self.path_p = [e for e in path]
        if node.val == q.val:  # 记录q的路径
            self.path_q = [e for e in path]
        self.traversal(node.left, p, q, path)
        self.traversal(node.right, p, q, path)
        path.pop()  # 回溯

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path = []
        self.traversal(root, p, q, path)
        common_len = len(set(self.path_p) & set(self.path_q))  # 两者求交集，就是公共祖先的路径
        return self.path_q[common_len - 1]  # common_len - 1所在位置节点