# 53. 最大子数组和
# https://programmercarl.com/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C%EF%BC%88%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%89.html
# https://leetcode.cn/problems/maximum-subarray/description/

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)  # dp[i]为nums[:i+1]的连续子数组的最大和
        max_sub = float('-inf')
        for i in range(1, len(nums) + 1):
            dp[i] = max(dp[i - 1] + nums[i - 1], nums[i - 1])  # 继续加，或者从头开始
            max_sub = max(dp[i], max_sub)
        return max_sub

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
