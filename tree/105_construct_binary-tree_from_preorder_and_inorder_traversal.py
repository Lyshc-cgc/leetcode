# 105. 从前序与中序遍历序列构造二叉树
# https://programmercarl.com/0106.%E4%BB%8E%E4%B8%AD%E5%BA%8F%E4%B8%8E%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E6%80%9D%E8%B7%AF
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traversal(self, preorder: List[int], inorder: List[int]):
        # 终止条件
        if len(inorder) == 0:
            return None

        # 1. 寻找分割点
        val = preorder[0]
        node = TreeNode(val)
        if len(preorder) == 1:  # 叶子结点
            return node

        deli_index = -1
        for idx in range(len(inorder)):
            if inorder[idx] == val:
                deli_index = idx
                break

        # 2. 切分左中序和右中序，左闭右开
        left_inorder, right_inorder = inorder[:deli_index], inorder[deli_index + 1:]

        # 3. 根据左中序和右中序长度切分左后序和右后序
        start = 1  # 排除第一个元素
        pre_deli = start + len(left_inorder)
        left_preorder, right_preorder = preorder[start: pre_deli], preorder[pre_deli:]

        # 4. 左孩子
        node.left = self.traversal(left_preorder, left_inorder)
        node.right = self.traversal(right_preorder, right_inorder)

        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.traversal(preorder, inorder)

if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    Solution().buildTree(preorder, inorder)