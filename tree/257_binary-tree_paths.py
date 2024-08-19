# 257. 二叉树的所有路径
# https://programmercarl.com/0257.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%B7%AF%E5%BE%84.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/binary-tree-paths/description/

from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traversal(self, node: Optional[TreeNode], path: List[int], all_paths: List[str]):
        if not node:
            return

        path.append(node.val)  # 中
        if not node.left and not node.right:  # 叶子结点, 打印路径
            res = ''
            if len(path) == 1:
                res = str(path[0])
            else:
                for e in path[:-1]:
                    res += str(e) + '->'
                res += str(path[-1])
            all_paths.append(res)
        self.traversal(node.left, path, all_paths)  # 左
        self.traversal(node.right, path, all_paths)  # 右
        path.pop()  # 返回时，需要将此节点去掉


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_res = []
        path = []  # stack
        if not root:
            return all_res
        self.traversal(root, path, all_res)
        return all_res
