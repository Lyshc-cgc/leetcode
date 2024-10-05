# 647. 回文子串
# https://programmercarl.com/0647.%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]  # dp[i][j]指示s[i: j + 1]是否为回文串

        count = 0
        i = len(s) - 1
        # 从下到上，从左到右
        while i >= 0:
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    # j - i == 0，字符串长度为1，如a
                    # j - i == 1，字符串长度为2，如aa
                    if i == j or j - i == 1:
                        count += 1
                        dp[i][j] = True
                    elif dp[i + 1][j - 1]:
                        count += 1
                        dp[i][j] = True
            i -= 1
        return count

if __name__ == '__main__':
    print(Solution().countSubstrings('aaa'))
