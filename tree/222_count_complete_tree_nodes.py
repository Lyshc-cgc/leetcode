# 222. 完全二叉树的节点个数
# https://programmercarl.com/0222.%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E8%8A%82%E7%82%B9%E4%B8%AA%E6%95%B0.html
# https://leetcode.cn/problems/count-complete-tree-nodes/description/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        stack = []
        count = 0
        if not root:
            return count
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:  # 不为空，遍历
                # 前序
                if node.right:  # 右
                    stack.append(node.right)
                if node.left:  # 左
                    stack.append(node.left)
                stack.append(node)
                stack.append(None)
            else:  # 为空，操作他的下一个节点
                node = stack.pop()
                count += 1
        return count