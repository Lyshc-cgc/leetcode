# 122. 买卖股票的最佳时机 II
# https://programmercarl.com/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII.html#%E6%80%9D%E8%B7%AF
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 计算每天买卖的收益
        profit_every_day = [prices[idx] - prices[idx - 1] for idx in range(len(prices)) if idx > 0]
        # 只收集正收益
        profit = sum([e for e in profit_every_day if e > 0])
        return profit

