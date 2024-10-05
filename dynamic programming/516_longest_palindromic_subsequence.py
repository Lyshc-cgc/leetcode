# 516. 最长回文子序列
# https://programmercarl.com/0516.%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E5%BA%8F%E5%88%97.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/longest-palindromic-subsequence/description/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]  # dp[i][j]表示s[i: j + 1]的最大回文子序列长度
        i = len(s) - 1
        while i >= 0:
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i == 0:
                        dp[i][j] = 1  # 相当于初始化
                    else:
                        # 以s[i+1:j]为中心，往外扩两个长度,加入s[i]和s[j]
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # 沿用s[i:j](加入s[i],不加入s[j])或s[i+1:j + 1](加入s[j],不加入s[i])中的最长回文子序列长度
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
            i -= 1
        return dp[0][-1]

if __name__ == '__main__':
    print(Solution().longestPalindromeSubseq("cbbd"))
