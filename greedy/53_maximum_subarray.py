# 53. 最大子数组和
# https://programmercarl.com/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.html#%E6%80%9D%E8%B7%AF
# https://leetcode.cn/problems/maximum-subarray/description/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = float('-inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > max_val:  # 当前累积和大于max时才记录
                max_val = count
            if count <= 0:  # 当前累积和小于等于0，重新累积
                count = 0
        return max_val

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))
