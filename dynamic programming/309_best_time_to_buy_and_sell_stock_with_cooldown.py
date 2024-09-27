# 309. 买卖股票的最佳时机含冷冻期
# https://programmercarl.com/0309.%E6%9C%80%E4%BD%B3%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E6%97%B6%E6%9C%BA%E5%90%AB%E5%86%B7%E5%86%BB%E6%9C%9F.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        # 长度大于等于2才有用
        dp = [[0,0,0] for _ in range(len(prices))]  # 3个状态，对应持股，不持股，冷冻期
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])  # 要么维持现状, 要么在上一天为冷冻期时买入
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])  # 要么维持现状, 要么在上一天为持股状态时卖出
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])  # 冷静期，可以维持现状（即在冷冻期之后，不操作），也可以由上一天卖出时决定
        return max(dp[-1][1], dp[-1][2])

if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    print(Solution().maxProfit(prices))