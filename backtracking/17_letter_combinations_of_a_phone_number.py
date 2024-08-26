# 17. 电话号码的字母组合
# https://programmercarl.com/0017.%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/

from typing import List

class Solution:
    def __init__(self):
        self.mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.path = []
        self.result = []

    def backtracing(self, digits: str, start_idx: int):
        if start_idx == len(digits):
            if len(self.path) == 0:
                return
            else:
                self.result.append(''.join([e for e in self.path]))
                return

        digit = digits[start_idx]
        chs = self.mapping[digit]
        for e in chs:  # 选择
            self.path.append(e)
            self.backtracing(digits, start_idx + 1)
            self.path.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        self.backtracing(digits, 0)
        return self.result

if __name__ == '__main__':
    digits = "2"
    print(Solution().letterCombinations(digits))
