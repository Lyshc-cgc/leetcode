# 406. 根据身高重建队列
# https://programmercarl.com/0406.%E6%A0%B9%E6%8D%AE%E8%BA%AB%E9%AB%98%E9%87%8D%E5%BB%BA%E9%98%9F%E5%88%97.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/queue-reconstruction-by-height/description/
from typing import List
class Node:
    def __init__(self, val, k, next=None):
        self.val = val
        self.k = k
        self.next = next

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先按身高降序排列,再按k排序
        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))

        dummy_head = Node(-1, -1)

        # 按照k来插入
        for e in sorted_people:
            cur = dummy_head
            k = e[-1]
            while k:
                cur = cur.next
                k -= 1
            cur.next = Node(e[0], e[1], cur.next)

        res = []
        cur = dummy_head.next
        while cur:
            res.append([cur.val, cur.k])
            cur = cur.next
        return res

if __name__ == '__main__':
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    print(Solution().reconstructQueue(people))





