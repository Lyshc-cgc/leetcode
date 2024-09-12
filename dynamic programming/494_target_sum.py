# 494. 目标和
# https://programmercarl.com/0494.%E7%9B%AE%E6%A0%87%E5%92%8C.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/target-sum/description/
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 将nums分成两堆
        # 一堆为n = (target +sum(nums)) // 2, 负责正数部分
        # 一堆为m = sum(nums) - n = (sum(nums) - target) // 2， 负责负数部分，不用管他了
        # dp[i][j] 表示从[0, i]中任意选物品加入容量为j的背包，将其装满的方案数
        nums_sum = sum(nums)
        if (target + nums_sum) % 2 == 1:  # 是奇数，无法被2整除
            return 0
        if nums_sum < abs(target):
            return 0
        n = (target + nums_sum) // 2
        dp = [[0] * (n + 1) for _ in range(len(nums))]

        # 1. 初始化
        if nums[0] == 0:
            dp[0][0] = 2  # 要么不装，要么装0，方案为2
        else:
            dp[0][0] = 1  # 背包容量为0，不装任何物品，方案为1
        if 0 < nums[0] <= n:  # 当nums[0]小于等于背包容量的时候才能初始化为1，否则为0
            dp[0][nums[0]] = 1  # 使用物品0把容量nums[0]的背包装满只有1种方法

        # 2. dp
        for i in range(1, len(nums)):
            for j in range(n + 1):  # 数字有0，所以容量可以从0开始遍历
                if j < nums[i]:
                    dp[i][j] = dp[i - 1][j]  # 不能放下nums[i]
                else:
                    # 不放nums[i]有dp[i - 1][j]种方法
                    # 放nums[i]，直接在dp[i - 1][j - nums[i]]基础上就可直接放入nums[i]
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]

        return dp[-1][-1]

    def findTargetSumWays0(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)  # 计算nums的总和
        if abs(target) > total_sum:
            return 0  # 此时没有方案
        if (target + total_sum) % 2 == 1:
            return 0  # 此时没有方案
        target_sum = (target + total_sum) // 2  # 目标和

        # 创建二维动态规划数组，行表示选取的元素数量，列表示累加和
        dp = [[0] * (target_sum + 1) for _ in range(len(nums) + 1)]

        # 初始化状态
        dp[0][0] = 1

        # 动态规划过程
        for i in range(1, len(nums) + 1):
            for j in range(target_sum + 1):
                dp[i][j] = dp[i - 1][j]  # 不选取当前元素
                if j >= nums[i - 1]:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]  # 选取当前元素

        return dp[len(nums)][target_sum]  # 返回达到目标和的方案数


if __name__ == '__main__':
    nums = [0,0,0,0,0,0,0,0,1]
    target = 1
    print(Solution().findTargetSumWays(nums, target))