# 27. 移除元素
# https://leetcode.cn/problems/remove-element/
from typing import List

class Solution:
    """
    交叉指针，本人猪脑容易写错
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        if len(nums) != 0:
            while(left <= right):
                while (nums[left] != val and left <= right):  # 找到左边第一个val
                    left += 1
                while (nums[right] == val and left <= right):  # 找到右边第一非val
                    right -= 1
                if (left < right):
                    nums[left] = nums[right]  # 覆盖
                    left += 1
                    right -= 1
        return left
class Solution2:
    """
    快慢指针
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != val:  # 当fast指针发现非val值，将他转移到slow指针指向的位置
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(Solution().removeElement(nums, val))