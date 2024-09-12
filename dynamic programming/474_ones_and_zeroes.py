# 474. 一和零
# https://programmercarl.com/0474.%E4%B8%80%E5%92%8C%E9%9B%B6.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/ones-and-zeroes/description/

from typing import List
from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 重量是两个维度，记录可以装的物品（字符串）数
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            sc = Counter(s)
            i = m  # 最多m个0，n个1
            while i >= sc['0']:  # 行记录0
                j = n  # 列记录1
                while j >= sc['1']:
                    dp[i][j] = max(dp[i][j], dp[i - sc['0']][j - sc['1']] + 1)  # 要么不拿该字符串，要么拿（物品数+1）
                    j -= 1
                i -= 1

        return dp[m][n]

if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    print(Solution().findMaxForm(strs, m, n))