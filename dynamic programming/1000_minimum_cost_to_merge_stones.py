# https://leetcode.cn/problems/minimum-cost-to-merge-stones/description/
# 区间dp
from sys import prefix
from typing import List

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        dp = [[float('inf')] * len(stones) for _ in range(len(stones))]  # dp[i][j] 表示合并stones[i:j+1]所需最低代价
        prefix_sum = [0] * (len(stones) + 1)

        # 计算前缀和
        for i in range(len(stones)):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]

        for i in range(len(stones)):
            dp[i][i] = 0
        remain_len = len(stones) - k + 1 # 合并后剩余长度. 刚开始 默认各石头合并了自身
        incre = k - 1
        while remain_len > 0:
            # 区间dp本质上是左上到右下斜着遍历， 根据需要平移需要遍历的斜线
            for start in range(0, remain_len):  # 遍历起点, 起点可选择的位置也随着合并而减少
                end = start + incre # 终点，其沿着dp table每次向右移动k - 1步 闭区间.
                for i, j in zip(range(start, start + k),range(end - k + 1, end + 1)):
                    # 在dp[start][end]左下角的位置中找最小代价
                    # 从dp[start][end - k + 1], dp[start + 1][end - k + 2],....dp[start + k - 1][end] 找到最小代价
                    # 即先合并stones[start: end - k + 1]| dp[start + 1: end - k +2]| dp[start + k - 1:end]
                    dp[start][end] = min(dp[start][end], dp[i][j] + prefix_sum[end + 1] - prefix_sum[start])
            incre += k - 1  # end向右移动k - 1步
            remain_len =  remain_len - k + 1
        if dp[0][-1] == float('inf'):  # 在此k值下，不可能合并
            return -1
        return dp[0][-1]

if __name__ == '__main__':
    stones = [3, 2, 4, 1]
    K = 2
    print(Solution().mergeStones(stones, K))