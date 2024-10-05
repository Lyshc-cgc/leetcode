# 674. 最长连续递增序列
# https://programmercarl.com/0674.%E6%9C%80%E9%95%BF%E8%BF%9E%E7%BB%AD%E9%80%92%E5%A2%9E%E5%BA%8F%E5%88%97.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/longest-continuous-increasing-subsequence/description/

from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_len = 1
        dp = [1] * len(nums)  # dp[i]表示以nums[i]结尾的子序列 最长连续递增子序列 的长度
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # 要求连续，所以只需要和前一个位置的 nums[i-1]结尾的子序列相比较 即可
                dp[i] = dp[i - 1] + 1
                max_len = max(dp[i], max_len)
        return max_len

if __name__ == '__main__':
    nums = [1,3,5,4,7]
    print(Solution().findLengthOfLCIS(nums))