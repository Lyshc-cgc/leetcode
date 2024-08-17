# 347. 前 K 个高频元素
# https://programmercarl.com/0347.%E5%89%8DK%E4%B8%AA%E9%AB%98%E9%A2%91%E5%85%83%E7%B4%A0.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/top-k-frequent-elements/description/
import heapq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = dict()
        pri_que = []
        for e in nums:
            record[e] = record.get(e, 0) + 1

        for num, freq in record.items():
            heapq.heappush(pri_que, (freq, num))  # 根据v来排序，默认最小堆
            if len(pri_que) > k:
                heapq.heappop(pri_que)

        res = [heapq.heappop(pri_que)[-1] for _ in range(len(pri_que))]
        return res[::-1]


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2

    print(Solution().topKFrequent(nums, k))