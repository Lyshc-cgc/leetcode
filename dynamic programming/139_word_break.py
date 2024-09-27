# 139. 单词拆分
# https://programmercarl.com/0139.%E5%8D%95%E8%AF%8D%E6%8B%86%E5%88%86.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/word-break/description/

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)  # dp[j]表示s[0:j]（长度为j）的字符串可以被截取为字典里单词
        dp[0] = True
        wordDict = set(wordDict)
        for j in range(1, len(s) + 1):  # 字符串右边界，相当于背包容量
            for i in range(j):  # 字符串左边界，相当于遍历物品
                sub_str = s[i:j]  # 截取字符串
                # 只有当[i:j]截取的字符串在字典里, 并且dp[i]为True，才能说明dp[j]为True
                if sub_str in wordDict and dp[i]:
                    dp[j] = True
        return dp[-1]

if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution().wordBreak(s, wordDict))
