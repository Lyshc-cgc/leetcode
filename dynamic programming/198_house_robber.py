# 198. 打家劫舍
# https://programmercarl.com/0198.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8D.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/house-robber/description/

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))  # dp[i]，到达第i个房间的最高价值
        dp[0] = nums[0]
        if len(nums) == 1:
            return dp[0]

        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # dp[i-2] + nums[i]是房间i-1不拿，拿第i个物品的最大价值.dp[i-2]里的物品可以不偷，也可以偷。只要跳过i-1房间，那i是一定可以拿的
            # dp[i - 1] 是拿房间i-1的最大价值。
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


if __name__ == '__main__':
    nums = [2,1,1,2]
    print(Solution().rob(nums))