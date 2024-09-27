# 188. 买卖股票的最佳时机 IV
# https://programmercarl.com/0188.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIV.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/description/

from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp  = [[0] * (2 * k + 1) for _ in range(len(prices))]  # k * 2个状态，对应第1次持股，第1次不持股，第2次持股，第2次不持股...第k次持股，第k次不持股
        # dp[i][0]  恒为0，表示无操作时的资金
        for i in range(k):
            # dp[0][1], dp[0][3], dp[0][5]... dp[0][2i + 1]
            dp[0][i * 2 + 1] = -prices[0]  # 第k天买入，卖出，再买入

        for i in range(1, len(prices)):
            for j in range(k):
                dp[i][2 * j + 1] = max(dp[i - 1][2 * j + 1], dp[i - 1][2 * j] - prices[i])  # 第j次持有股,要么维持原状，要么在第j - 1次不持股的基础上买入
                dp[i][2 * j + 2] = max(dp[i - 1][2 * j + 2], dp[i - 1][2 * j + 1] + prices[i])  # 第j次不持股，要么维持原状，要么在第j次不持股的基础上买入

        return dp[-1][-1]

if __name__ == '__main__':
    k = 2
    prices = [3,2,6,5,0,3]
    print(Solution().maxProfit(k, prices))