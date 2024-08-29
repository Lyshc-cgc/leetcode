# 455. 分发饼干
# https://programmercarl.com/0455.%E5%88%86%E5%8F%91%E9%A5%BC%E5%B9%B2.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/assign-cookies/description/

from typing import  List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        # 小饼干优先分配给小胃口的人
        idx = 0
        count = 0
        for e in g:
            while idx < len(s) and e > s[idx]:  # 找到第一个符合e胃口的饼干
                idx += 1
            if idx < len(s) and e <= s[idx]:
                count += 1
                idx += 1  # 移动到下一块饼干
        return count
        

