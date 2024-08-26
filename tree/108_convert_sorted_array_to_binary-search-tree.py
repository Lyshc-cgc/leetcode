# 108. 将有序数组转换为二叉搜索树
# https://programmercarl.com/0108.%E5%B0%86%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E8%BD%AC%E6%8D%A2%E4%B8%BA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traversal(self, nums: List[int], start: int, end: int):
        if end - start == 1:  # 叶子节点
            return TreeNode(nums[start])
            # 中
        if end > start:  # 左闭右开，只能让end大于start， 小于等于定义空
            mid = (end + start) // 2  # left + (right - left) // 2防止越界
            node = TreeNode(nums[mid])
            node.left = self.traversal(nums, start, mid)  # 左
            node.right = self.traversal(nums, mid + 1, end)  # 右
            return node
        else:
            return None

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.traversal(nums, 0, len(nums))
        return root
