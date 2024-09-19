# 377. 组合总和 Ⅳ
# https://programmercarl.com/0377.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C%E2%85%A3.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/combination-sum-iv/description/

from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)  # dp[j]表示凑出j有dp[j]种排列数
        dp[0] = 1
        # 计算排列数，外围遍历容量，内层遍历物品
        for j in range(1, target + 1):
            for i in range(len(nums)):
                if j >= nums[i]:
                    dp[j] = dp[j] + dp[j - nums[i]]

        return dp[-1]

if __name__ == '__main__':
    print(Solution().combinationSum4(nums = [1,2,3], target = 4))
