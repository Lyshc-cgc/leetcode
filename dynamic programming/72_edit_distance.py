# 72. 编辑距离
# https://programmercarl.com/0072.%E7%BC%96%E8%BE%91%E8%B7%9D%E7%A6%BB.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j]， 表示word1[:i] 转换成word2[:j] 所需最少操作数
        dp = [[float('inf')] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word2) + 1):
            dp[0][i] = i
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i- 1] == word2[j - 1]:  # 就不用操作了
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1  # 找最小的， 进行一次操作

        return dp[-1][-1]

if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(Solution().minDistance(word1, word2))