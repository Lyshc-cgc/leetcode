# 977. 有序数组的平方
# https://programmercarl.com/0209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.html
# https://leetcode.cn/problems/squares-of-a-sorted-array/description/
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        相向指针，由于数组是非递减的，那么平方最大值一定在"外围"的位置
        :param nums:
        :return:
        """
        left, right = 0, len(nums) - 1
        res = []
        while(left <= right):
            num_left = nums[left] ** 2
            num_right = nums[right] ** 2
            if num_left <= num_right:  # 谁大就把谁放进去，再移动指针
                res.append(num_right)
                right -= 1
            else:
                res.append(num_left)
                left += 1

        return res[::-1]

if __name__ == '__main__':
    nums = [-7,-3,2,3,11]
    print(Solution().sortedSquares(nums))