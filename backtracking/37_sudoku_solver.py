# 37. 解数独
# https://www.programmercarl.com/0037.%E8%A7%A3%E6%95%B0%E7%8B%AC.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/sudoku-solver/description/
from typing import List

class Solution:
    def is_valid(self, board, row, col, num):
        # 检查列
        for i in range(len(board)):
            if board[i][col] == num:
                return False

        # 检查行
        for i in range(len(board)):
            if board[row][i] == num:
                return False

        # 检查九宫格
        start_row = row // 3 * 3
        start_col = col // 3 * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def backtracing(self, board):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != '.':
                    continue
                for num in range(1, 10):
                    if self.is_valid(board, row, col, str(num)):  # 该位置合法
                        board[row][col] = str(num)
                        if self.backtracing(board):  # 若找到一组解法，直接返回
                            return True
                        board[row][col] = '.'
                return False  # 9个数都用完了，有问题，回退
        return True  # 没有False，都填好数字了，直接返回True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracing(board)


