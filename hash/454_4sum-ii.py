# 454. 四数相加 II
# https://programmercarl.com/0454.%E5%9B%9B%E6%95%B0%E7%9B%B8%E5%8A%A0II.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/4sum-ii/description/

from typing import List
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        records = dict()
        for i in nums1:
            for j in nums2:
                records[i+j] = records.get(i+j, 0) + 1
        count = 0
        for i in nums3:
            for j in nums4:
                count += records.get(0-(i+j), 0)
        return count

if __name__ == '__main__':
    print(Solution().fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))  # 2
    print(Solution().fourSumCount([0], [0], [0], [0]))  # 1
    print(Solution().fourSumCount([1,1,1], [1,1,1], [1,1,1], [1,1,1]))  # 0