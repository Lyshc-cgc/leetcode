# 343. 整数拆分
# https://programmercarl.com/0343.%E6%95%B4%E6%95%B0%E6%8B%86%E5%88%86.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/integer-break/description/

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])  # 分别是不拆， 拆成俩数和拆成多个数（拆分i-j）
                # dp[i] = max(dp[i], dp[j] * dp[i - j])
        return dp[-1]

if __name__ == '__main__':
    print(Solution().integerBreak(10))
