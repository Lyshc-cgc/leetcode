# 435. 无重叠区间
# https://programmercarl.com/0435.%E6%97%A0%E9%87%8D%E5%8F%A0%E5%8C%BA%E9%97%B4.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/non-overlapping-intervals/description/

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 和435很像，弓箭的数量就是非交叉区间的数量。再用总长-非交叉区间数量即可得移除区间总数

        # 这里是统计重叠区间
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key=lambda x: x[0])  # 按起始位置排序

        count = 0  # 记录重叠区间数量
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:  # 重叠
                count += 1
                intervals[i][1] = min(intervals[i][1], intervals[i - 1][1])  # 更新最小右边界，防止重复计数
        return count


