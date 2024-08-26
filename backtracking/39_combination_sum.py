# 39. 组合总和
# https://programmercarl.com/0039.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/combination-sum/description/
from typing import List

class Solution:
    def __init__(self):
        self.comb = []
        self.res = []

    def backtracing(self, candidates: List[int], target: int, start_idx: int):
        if sum(self.comb) == target:
            self.res.append([e for e in self.comb])
            return

        for i in range(start_idx, len(candidates)):
            num = candidates[i]
            if sum(self.comb) + num > target:  # candidates是有序的，此时若和大于target，后续递归和遍历一定不满足
                return
            self.comb.append(num)
            self.backtracing(candidates, target, i)  # 尽量先使用自己来凑
            self.comb.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        self.backtracing(candidates, target, 0)
        return self.res

if __name__ == '__main__':
    candidates = [2,3,5]
    target = 8
    print(Solution().combinationSum(candidates, target))