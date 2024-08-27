# 51. N 皇后
# https://www.programmercarl.com/0051.N%E7%9A%87%E5%90%8E.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/n-queens/description/

from typing import List
class Solution:
    def __init__(self):
        self.chessboard = []
        self.res = []

    def valid(self, row, col, n):
        # 检查列
        for row_idx in range(row):
            if self.chessboard[row_idx][col] == 'Q':
                return False
            row_idx -= 1

        # 检查45度角
        row_idx, col_idx = row - 1, col - 1
        while row_idx >= 0 and col_idx >= 0:
            if self.chessboard[row_idx][col_idx] == 'Q':
                return False
            row_idx -= 1
            col_idx -= 1

        # 检查135度角
        row_idx, col_idx = row - 1, col + 1
        while row_idx >= 0 and col_idx < n:
            if self.chessboard[row_idx][col_idx] == 'Q':
                return False
            row_idx -= 1
            col_idx += 1
        return True

    def backtracing(self, row, col, n):
        if row == n or col == n:
            self.res.append([''.join(e) for e in self.chessboard])
            return

        for col in range(n):
            if self.valid(row, col, n):
                self.chessboard[row][col] = 'Q'
                self.backtracing(row + 1, 0, n)
                self.chessboard[row][col] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.chessboard = [['.'] * n for _ in range(n)]
        self.backtracing(0, 0, n)
        return self.res
