# 1005. K 次取反后最大化的数组和
# https://programmercarl.com/1005.K%E6%AC%A1%E5%8F%96%E5%8F%8D%E5%90%8E%E6%9C%80%E5%A4%A7%E5%8C%96%E7%9A%84%E6%95%B0%E7%BB%84%E5%92%8C.html
# https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/description/

from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)  # 从小到大排列，负数在前
        while k:
            if nums[0] == 0:
                break  #遇到0时，直接让k全部对他操作，数组和就不变了
            if nums[0] < 0:  # 若为负数，则取反
                nums.append(nums.pop(0) * -1)
            else:  # 若为正数，此时重排序后，直接对最小正数进行操作作
                nums = sorted(nums)
                nums[0] *= (-1) ** k
                break
            k -= 1
        return sum(nums)