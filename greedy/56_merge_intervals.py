# 56. 合并区间
# https://programmercarl.com/0056.%E5%90%88%E5%B9%B6%E5%8C%BA%E9%97%B4.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/merge-intervals/description/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])  # 按起始位置升序
        left = intervals[0][0]
        right = intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > right:  # 没挨着
                res.append([left, right])  # 记录
                left = intervals[i][0]  # 重新记录左边界
            right = max(intervals[i][1], right)
        res.append([left, right])  # 最后一个
        return res
