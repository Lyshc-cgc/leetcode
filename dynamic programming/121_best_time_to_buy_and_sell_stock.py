# 121. 买卖股票的最佳时机
# https://programmercarl.com/0121.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA.html#%E6%80%9D%E8%B7%AF
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0] 表示第i天持有股票时的最多现金
        # dp[i][1] 表示第i天不持有股票时的最多现金
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]  # 第0天持有股票，即买入第0天的股票
        for i in range(1, len(prices)):
            # 第i天持有股票时的现金，可以以前就持有，今天不买，即dp[i - 1][0]
            # 或者今天买入。由于只买一次，所以买入时的初始资金为0。
            # 假如可以多次买卖，则初始资金为dp[i - 1][1],即第i-1天不持有股票时的资金
            dp[i][0] = max(dp[i - 1][0], 0 - prices[i])

            # 不持有，可以以前就不持有。维持现状，dp[i - 1][1]
            # 也可以将之前持有的股票卖出。
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

        return max(dp[-1][0], dp[-1][1])


