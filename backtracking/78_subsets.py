# 78. 子集
# https://www.programmercarl.com/0078.%E5%AD%90%E9%9B%86.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/subsets/description/
from typing import List

class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def backtracing(self, nums, start):
        # if start == len(nums):
        #     self.res.append([e for e in self.path])
        #     return

        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.backtracing(nums, i + 1)
            self.path.pop()
        # 加上自身
        self.res.append([e for e in self.path])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtracing(nums, 0)
        return self.res

if __name__ == '__main__':
    nums = [1,2,2,2]
    print(Solution().subsets(nums))

