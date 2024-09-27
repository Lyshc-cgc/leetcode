# 213. 打家劫舍 II
# https://programmercarl.com/0213.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DII.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/house-robber-ii/description/

from typing import List

class Solution:
    def rob_range(self, nums: List[int], start, end) -> int:
        """
        抢劫nums[start: end]的最高金额
        :param nums:
        :param start:
        :param end:
        :return:
        """
        dp = [0] * (end - start)  # dp[i]表示考虑偷窃前i个房子的最高金额
        dp[0] = nums[start]
        if end - start == 1:  # 长度只有1
            return dp[0]
        # 长度大于1
        dp[1] = max(nums[start], nums[start + 1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 2] + nums[start + i], dp[i - 1])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # 环状dp,需要数组长度大于1
        # 1. 不考虑最后一个房间
        val0 = self.rob_range(nums, 0, len(nums) - 1)

        # 2. 不考虑第一个房间
        val1 = self.rob_range(nums, 1, len(nums))

        return max(val0, val1)