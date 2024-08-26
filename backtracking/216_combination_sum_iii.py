# 216. 组合总和 III
# https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/combination-sum-iii/description/

from typing import List

class Solution:
    def __init__(self):
        self.result = []
        self.comb = []

    def backtracing(self, k: int, n: int, start_idx: int):
        if sum(self.comb) == n and len(self.comb) == k:
            self.result.append([e for e in self.comb])
            return
        # 走到这里，说明还必须得继续选择数字往里面加
        for i in range(start_idx, 10):  # 使用数字1到9
            # start_idx 是当前最小的数字，遇到以下情况剪枝
            # 1) 若其比n还大
            # 2)或其加入到comb中和大于n
            if i > n or sum(self.comb) + i > n:
                return
            self.comb.append(i)
            self.backtracing(k, n, i + 1)
            self.comb.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtracing(k, n, 1)
        return self.result
