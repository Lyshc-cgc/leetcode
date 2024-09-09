# 63. 不同路径 II
# https://programmercarl.com/0063.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84II.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/unique-paths-ii/description/

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        # 初始化
        for row in range(len(obstacleGrid)):
            if obstacleGrid[row][0] == 0:  # 没有障碍才为1
                dp[row][0] = 1  # 只有一种走法，向下走
            else:
                break  # 遇到障碍，后面就不管了
        for col in range(len(obstacleGrid[0])):
            if obstacleGrid[0][col] == 0:
                dp[0][col] = 1  # 只有一种走法，向右走
            else:
                break
        # dp
        for row in range(1, len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[0])):
                if obstacleGrid[row][col] == 0:  # 没有障碍才更新
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]

if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles([[1,0]]))