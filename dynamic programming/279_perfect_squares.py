# 279. 完全平方数
# https://programmercarl.com/0279.%E5%AE%8C%E5%85%A8%E5%B9%B3%E6%96%B9%E6%95%B0.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/perfect-squares/description/

import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)  # dp[j]表示和为j的完全平方数的最少数量
        dp[0] = 0
        for i in range(1, int(math.sqrt(n)) + 1):  # 物品， 遍历到math.sqrt(n)即可。因为要满足 i * i <= j
            for j in range(1, n + 1):  # 容量
                num = i ** 2
                # dp[j]是不放num时的完全平方数的最少数量
                # dp[j - num]是预留出num的容量， +1则是把num放进去
                if j >= num:
                    dp[j] = min(dp[j], dp[j - num] + 1)

        return dp[-1]

if __name__ == '__main__':
    print(Solution().numSquares(13))