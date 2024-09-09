# 509. 斐波那契数
# https://programmercarl.com/0509.%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.html#%E6%80%9D%E8%B7%AF
# https://leetcode.cn/problems/fibonacci-number/description/

class Solution:
    def fib(self, n: int) -> int:
        dp = [0] * (n + 1)
        if n >= 1:
            dp[1] = 1
        else:
            return dp[n]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

if __name__ == '__main__':
    print(Solution().fib(0))