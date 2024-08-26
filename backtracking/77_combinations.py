# 77. 组合
# https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/combinations/description/

from typing import List

class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def back_tracing(self, n: int, k: int, start_idx: int):
        if len(self.path) == k:
            self.result.append([e for e in self.path])
            return
        for i in range(start_idx, n + 1):
            if n - i + 1 < k - len(self.path):  # 必须满足剩余元素个数(n-i+1) >= 所需元素个数(k - len(self.path))
                # 剪枝
                return
            self.path.append(i)
            self.back_tracing(n, k, i + 1)
            self.path.pop()
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.back_tracing(n, k, 1)
        return self.result

if __name__ == '__main__':
    n = 4
    k = 2
    print(Solution().combine(n, k))
