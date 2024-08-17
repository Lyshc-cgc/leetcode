# 239. 滑动窗口最大值
# https://programmercarl.com/0239.%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/sliding-window-maximum/description/

from typing import List
from collections import deque
import heapq

class MyQueue:
    def __init__(self):
        self.q = deque()

    def pop(self, value):
        """
        当value（滑动窗口排出的值）为队列出口时的元素时，才pop
        :param value:
        :return:
        """
        if self.q and value == self.q[0]:
            self.q.popleft()

    def push(self, value):
        """
        当value小于队列中最后一个元素时，才push，满足单调递减。否则，不断pop队列的最后一个元素，直到满足单调递减
        :param value:
        :return:
        """
        while self.q and self.q[-1] < value:
            self.q.pop()
        self.q.append(value)

    def get_front(self):
        return self.q[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = MyQueue()
        res_list = []
        for i in range(k):
            q.push(nums[i])
        res_list.append(q.get_front())
        for j in range(1, len(nums) - k + 1):
            pop_value = nums[j - 1]
            q.pop(pop_value)
            push_value = nums[j + k - 1]
            q.push(push_value)
            res_list.append(q.get_front())
        return res_list


if __name__ == '__main__':
    nums  = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(Solution().maxSlidingWindow0(nums, k))