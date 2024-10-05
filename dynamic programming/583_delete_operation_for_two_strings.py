# 583. 两个字符串的删除操作
# https://programmercarl.com/0583.%E4%B8%A4%E4%B8%AA%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E5%88%A0%E9%99%A4%E6%93%8D%E4%BD%9C.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/delete-operation-for-two-strings/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 1. 先求最长公共子序列长度a
        # 2. 然后各自减去改长度,加和即为需要删除的步骤 len(word1) - a + len(word2) - a
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lcs_len = dp[-1][-1]
        return len(word1) - lcs_len + len(word2) - lcs_len
