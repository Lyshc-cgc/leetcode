# 122. 买卖股票的最佳时机 II
# https://programmercarl.com/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII%EF%BC%88%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%89.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]  # 持有股票
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])  # 持有
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])  # 不持有

        return max(dp[-1][0], dp[-1][1])

if __name__ == '__main__':
    prices = [7,6,4,3,1]
    print(Solution().maxProfit(prices))