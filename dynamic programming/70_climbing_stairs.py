# 70. 爬楼梯
# https://programmercarl.com/0070.%E7%88%AC%E6%A5%BC%E6%A2%AF.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        if n <= 1:
            return n
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

if __name__ == '__main__':
    print(Solution().climbStairs(3))