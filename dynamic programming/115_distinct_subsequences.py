# 115. 不同的子序列
# https://programmercarl.com/0115.%E4%B8%8D%E5%90%8C%E7%9A%84%E5%AD%90%E5%BA%8F%E5%88%97.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/distinct-subsequences/description/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]  # dp[i][j]表示s[:i]组合成t[:j]有dp[i][j]种方案
        for i in range(len(s) + 1):  # s中以任意字符结尾，通过删除元素 从而形成空字符的方法为1
            dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    # 要么使用s[i - 1]来匹配t[j - 1]，此时有dp[i - 1][j - 1]种方案
                    # 要么不使用s[i- 1]来匹配t[j - 1],此时有dp[i - 1][j]种方案。
                    # 1) 当s[i - 2] == t[j - 2]时，dp[i - 1][j]不为0
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]  # 不用s[i - 1]来匹配

        return dp[-1][-1]

if __name__ == '__main__':
    s = "babgbag"
    t = "bag"
    print(Solution().numDistinct(s, t))