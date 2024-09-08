# 452. 用最少数量的箭引爆气球
# https://programmercarl.com/0452.%E7%94%A8%E6%9C%80%E5%B0%91%E6%95%B0%E9%87%8F%E7%9A%84%E7%AE%AD%E5%BC%95%E7%88%86%E6%B0%94%E7%90%83.html
# https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/description/

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])  # 按照起始位置排序
        count = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]:  # 当前气球的起始位置大于上一个气球的结束位置,没挨着
                count += 1  # 多消耗一根箭
            else:
                # 将自己的结束位置调整为 能射爆的最大值
                # 更新重叠气球最小右边界
                points[i][1] = min(points[i][1], points[i - 1][1])
        return count