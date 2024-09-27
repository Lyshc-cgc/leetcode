# 123. 买卖股票的最佳时机 III
# https://programmercarl.com/0123.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIII.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/description/

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp  = [[0,0,0,0] for _ in range(len(prices))]  # 4个状态，对应第一次持股，第1次不持股，第2次持股，第2次不持股
        dp[0][0] = -prices[0]
        dp[0][2] = -prices[0]  # 第一天买入，卖出，再买入
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], 0 - prices[i])  # 第一次持有股
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])  # 第一次不持股
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i])  # 第二次持股.可以是维持原状，也可以是在第1次不持股后买入
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + prices[i])  # 第二次不持股，...，也可以是在第二次持股后卖出

        return dp[-1][-1]

if __name__ == '__main__':
    prices = [3,3,5,0,0,3,1,4]
    print(Solution().maxProfit(prices))