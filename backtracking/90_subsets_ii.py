# 90. 子集 II
# https://www.programmercarl.com/0090.%E5%AD%90%E9%9B%86II.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/subsets-ii/description/

from typing import List

class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def backtracing(self, nums, start):
        pre = -11
        for i in range(start, len(nums)):
            if pre == nums[i]:
                continue
            pre = nums[i]
            self.path.append(nums[i])
            self.backtracing(nums, i+1)
            self.path.pop()
        self.res.append(self.path[:])

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        self.backtracing(nums, 0)
        return self.res

if __name__ == '__main__':
    nums = [1,2,2,2,2]
    print(Solution().subsetsWithDup(nums))
