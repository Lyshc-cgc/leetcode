# 322. 零钱兑换
# https://programmercarl.com/0322.%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/coin-change/description/

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)  # dp[j]表示凑出金额j的最小硬币数量
        dp[0] = 0  # 凑0，默认为0
        # 外层物品
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                # dp[j]是不放coins[i]时的最小硬币数
                # dp[j - coins[i]]是预留出coins[i]， +1则是把coins[i]放进去
                if j >= coins[i]:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        if dp[-1] == float('inf'):  # 凑不出来，没有任何一种硬币组合能组成总金额
            return -1
        return dp[-1]

if __name__ == '__main__':
    print(Solution().coinChange(coins = [1], amount = 0))