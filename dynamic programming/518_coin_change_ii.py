# 518. 零钱兑换 II
# https://programmercarl.com/0518.%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2II.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/coin-change-ii/description/

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)  # dp[j] 表示装满容量为j的背包（金额）有多少种装法
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                if j > coins[i]:
                    dp[j] = dp[j] + dp[j - coins[i]]  # dp[j]是使用货币0到i-1填满amount的数目，dp[j - coins[j]]是在装满j - coins[j]的基础上直接加入货币i
                elif j == coins[i]:
                    dp[j] = dp[j] + 1  #
        # 排列数
        # for j in range(amount + 1):
        #     for i in range(len(coins)):
        #         if j > coins[i]:
        #             dp[j] = dp[j] + dp[j - coins[i]]  # dp[j]是使用货币0到i-1填满amount的数目，dp[j - coins[j]]是在装满j - coins[j]的基础上直接加入货币i
        #         elif j == coins[i]:
        #             dp[j] = dp[j] + 1  #
        return dp[-1]

if __name__ == '__main__':
    print(Solution().change(amount = 5, coins = [1, 2, 5]))
