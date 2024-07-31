# 59. 螺旋矩阵 II
# https://programmercarl.com/0059.%E8%9E%BA%E6%97%8B%E7%9F%A9%E9%98%B5II.html
# https://leetcode.cn/problems/spiral-matrix-ii/description/

from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 初始化矩阵
        matrix = [[0] * n for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 往右走(行不变，列加1), 往下走(行加1，列不变), 往左走(行不变，列减1),往上走(行-1，列不变)
        dir_index = 0  # 指示方向
        row, col = 0, -1  # 起始位置
        for num in range(1, n * n + 1):  # 1到n**2
            # 预先走一步
            pre_row = row + directions[dir_index][0]
            pre_col = col + directions[dir_index][1]
            if pre_row < n and pre_col < n and matrix[pre_row][pre_col] == 0:  # 没有越界或者没有遇到数字，则可以按原方向前进
                row, col = pre_row, pre_col
            else:  # 越界或碰到数字，需要改变方向再前进
                dir_index = (dir_index + 1) % len(directions)  # 取余，循环指针
                row += directions[dir_index][0]
                col += directions[dir_index][1]
            matrix[row][col] = num  # 前进！

        return matrix


if __name__ == '__main__':
    solution = Solution()
    n = 5
    print(solution.generateMatrix(n))