# 47. 全排列 II
# https://www.programmercarl.com/0047.%E5%85%A8%E6%8E%92%E5%88%97II.html
# https://leetcode.cn/problems/permutations-ii/


from typing import List

class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def backtracing(self, nums, used):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return

        seen = set()
        for idx, e in enumerate(nums):
            if used[idx] or e in seen:
                continue
            used[idx] = 1
            seen.add(e)
            self.path.append(e)
            self.backtracing(nums, used)
            self.path.pop()
            used[idx] = 0

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [0] * len(nums)
        self.backtracing(nums, used)
        return self.res