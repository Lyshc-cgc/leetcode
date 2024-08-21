# 106. 从中序与后序遍历序列构造二叉树
# https://programmercarl.com/0106.%E4%BB%8E%E4%B8%AD%E5%BA%8F%E4%B8%8E%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E6%80%9D%E8%B7%AF
# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def traversal(self, inorder: List[int], in_begin, in_end, postorder: List[int], post_begin, post_end):
        # 终止条件
        if in_begin == in_end:
            return None

        # 1. 寻找分割点
        val =  postorder[post_end - 1]
        node = TreeNode(val)
        if in_begin - in_end == 1:  # 叶子结点
            return node

        deli_index = -1
        for idx in range(in_begin, in_end):
            if inorder[idx] == val:
                deli_index = idx
                break

        # 2. 切分左中序和右中序，左闭右开
        left_inorder_begin = in_begin
        left_inorder_end = deli_index
        right_inorder_begin = deli_index + 1
        right_inorder_end = in_end

        # 3. 根据左中序和右中序长度切分左后序和右后序
        left_postorder_begin = post_begin
        left_postorder_end = post_begin + (left_inorder_end - left_inorder_begin)
        right_postorder_begin = left_postorder_end
        right_post_end = post_end - 1  # 排除最后一个元素

        # 4. 左孩子
        node.left = self.traversal(inorder, left_inorder_begin, left_inorder_end, postorder, left_postorder_begin, left_postorder_end)
        node.right = self.traversal(inorder, right_inorder_begin, right_inorder_end, postorder, right_postorder_begin, right_post_end)

        return node

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.traversal(inorder, 0, len(inorder), postorder, 0, len(postorder))