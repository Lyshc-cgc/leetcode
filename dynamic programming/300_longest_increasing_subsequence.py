# 300. 最长递增子序列
# https://programmercarl.com/0300.%E6%9C%80%E9%95%BF%E4%B8%8A%E5%8D%87%E5%AD%90%E5%BA%8F%E5%88%97.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/longest-increasing-subsequence/description/

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_len = 1
        dp = [1] * len(nums)  # dp[i] 表示以nums[i]结尾的子序列的最长上升子序列长度
        for i in range(1, len(nums)):  # 让nums[i] 依次与其之前的子序列结尾 nums[j]进行比较.
            for j in range(i):  # 由于不要求连续。所以需要和i之前的所有子序列比较
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    max_len = max(dp[i], max_len)

        return max_len

if __name__ == '__main__':
    nums = [1,3,6,7,9,4,10,5,6]
    print(Solution().lengthOfLIS(nums))
