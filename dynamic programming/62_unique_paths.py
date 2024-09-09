# 62. 不同路径
# https://programmercarl.com/0062.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/unique-paths/description/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        # 初始化
        for col in range(n):
            dp[0][col] = 1  # 只能向右走

        for row in range(m):
            dp[row][0] = 1  # 只能向下走

        # dp
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]  # 在原始的基础上，向下|右

        return dp[m - 1][n - 1]

if __name__ == '__main__':
    print(Solution().uniquePaths(3, 3))
