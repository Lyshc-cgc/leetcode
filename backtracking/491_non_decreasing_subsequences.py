# 491. 非递减子序列
# https://www.programmercarl.com/0491.%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/non-decreasing-subsequences/description/
from typing import List

class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def backtracing(self, nums, start):
        seen = set()
        for i in range(start, len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            if len(self.path) == 0 or nums[i] >= self.path[-1]:
                self.path.append(nums[i])
                self.backtracing(nums, i + 1)
                self.path.pop()
        # 过滤掉元素数量小于2的
        if len(self.path) >= 2:
            self.res.append([e for e in self.path])

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.backtracing(nums, 0)
        return self.res
