# 1. 两数之和
# https://programmercarl.com/0001.%E4%B8%A4%E6%95%B0%E4%B9%8B%E5%92%8C.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/two-sum/description/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()
        for idx, num in enumerate(nums):
            complete = target - num
            if complete in records:
                return [records[complete], idx]
            records[num] = idx

if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15], 9))  # [0,1]