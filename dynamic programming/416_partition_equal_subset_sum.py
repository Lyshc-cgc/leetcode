# 416. 分割等和子集
# https://programmercarl.com/0416.%E5%88%86%E5%89%B2%E7%AD%89%E5%92%8C%E5%AD%90%E9%9B%86.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/partition-equal-subset-sum/description/

from typing import List

class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        sum_num = sum(nums)
        if sum_num % 2 == 1:
            return False
        target = sum_num // 2
        dp = [0] * (target + 1)  # dp[j]表示背包容量为j时可以取得的最大价值
        for i in range(len(nums)):  # 外围遍历物品
            j = target
            while j >= nums[i]:
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
                j -= 1
        return dp[-1] == target  # dp[-1]为dp[target]，表示容量为target的子集中可以取得最大和，若其等于taget，说明该子集可以凑出target


if __name__ == '__main__':
    nums = [1,2,3,5]
    print(Solution().canPartition(nums))