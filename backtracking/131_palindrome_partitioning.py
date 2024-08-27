# 131. 分割回文串
# https://www.programmercarl.com/0131.%E5%88%86%E5%89%B2%E5%9B%9E%E6%96%87%E4%B8%B2.html
# https://leetcode.cn/problems/palindrome-partitioning/description/

from typing import  List

class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def backtracing(self, s, start_idx):
        if start_idx == len(s):
            self.res.append([e for e in self.path])
            return
        for i in range(start_idx, len(s)):
            str = s[start_idx: i + 1]  # 截取的子串[start_idx, i]  # 左闭右开
            if str == str[::-1]:
                self.path.append(str)
                self.backtracing(s, i + 1)  # 再在右边的子串中找回文串
                self.path.pop()
            # 若此分割不满足，则不用再往后割了，直接跳过

    def partition(self, s: str) -> List[List[str]]:
        self.backtracing(s, 0)
        return self.res

if __name__ == '__main__':
    s = 'aab'
    print(Solution().partition(s))
