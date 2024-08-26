# 40. 组合总和 II
# https://programmercarl.com/0040.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CII.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/combination-sum-ii/description/

from typing import List

class Solution:
    def __init__(self):
        self.comb = []
        self.res = []

    def back_tracing(self, candidates: List[int], target: int, start_idx: int):
        if sum(self.comb) == target:
            self.res.append([e for e in self.comb])
            return
        pre = 0
        for i in range(start_idx, len(candidates)):
            if candidates[i] == pre:  # 用过了,找下一个没用过的
                continue
            pre = candidates[i]
            if sum(self.comb) + candidates[i] > target:  # 或者和大于target
                return
            self.comb.append(candidates[i])
            self.back_tracing(candidates, target, i + 1)
            self.comb.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        self.back_tracing(candidates, target, 0)
        return self.res