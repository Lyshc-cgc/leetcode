# 332. 重新安排行程
# https://www.programmercarl.com/0332.%E9%87%8D%E6%96%B0%E5%AE%89%E6%8E%92%E8%A1%8C%E7%A8%8B.html#%E6%80%9D%E8%B7%AF
# https://leetcode.cn/problems/reconstruct-itinerary/description/

from typing import List

class Solution:
    def __init__(self):
        self.res = []

    def backtracing(self, tickets, src, itinerary):
        if len(self.res) == len(tickets) + 1:  # 满足条件，剪枝
            return
        while src in itinerary and len(itinerary[src]) > 0:
            tgt = itinerary[src].pop(0)  # 直接选第一个
            self.backtracing(tickets, tgt, itinerary)
        self.res.append(src)


    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda x: x[1])  # 根据目的地字典升序排列
        itinerary = dict()
        for src, tgt in tickets:
            if src in itinerary:
                itinerary[src].append(tgt)
            else:
                itinerary[src] = [tgt]

        self.backtracing(tickets, 'JFK', itinerary)
        return self.res[::-1]


