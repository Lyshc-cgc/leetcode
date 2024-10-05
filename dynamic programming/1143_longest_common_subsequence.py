# 1143. 最长公共子序列
# https://programmercarl.com/1143.%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/longest-common-subsequence/description/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]  # dp[i][j]表示 序列text1[:i](不包含i)与text2[:j] 的最长公共子序列长度
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:  # 下标减1才和字符串对应
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 此时最长公共子序列长度，要么为 text1[:i]与text2[:j-1]的最长重复子序列长度， dp[i][j - 1]
                    # 要么为nums2[:i - 1]和nums1[:j]的...， dp[i-1][j]
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

if __name__ == '__main__':
    print(Solution().longestCommonSubsequence("abcde", "ace"))