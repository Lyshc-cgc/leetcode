# 46. 全排列
# https://www.programmercarl.com/0046.%E5%85%A8%E6%8E%92%E5%88%97.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/permutations/description/

from typing import List

class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def backtracing(self, nums, used):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])

        for idx, e in enumerate(nums):

            if used[idx]:
                continue
            used[idx] = 1
            self.path.append(e)
            self.backtracing(nums, used)
            self.path.pop()
            used[idx] = 0
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [0] * len(nums)
        self.backtracing(nums, used)
        return self.res

if __name__ == '__main__':
    print(Solution().permute([1,1,2]))