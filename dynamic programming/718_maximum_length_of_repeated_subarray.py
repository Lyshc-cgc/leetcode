# 718. 最长重复子数组
# https://programmercarl.com/0718.%E6%9C%80%E9%95%BF%E9%87%8D%E5%A4%8D%E5%AD%90%E6%95%B0%E7%BB%84.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/maximum-length-of-repeated-subarray/description/

from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        max_len = 0
        dp = [[0] * (len(nums1) + 1) for _ in range(len(nums2) + 1)]  # dp[i][j] 表示序列 nums2[:i] 和nums1[:j]的重复子序列长度（从末尾算起）
        for i in range(1, len(nums2) + 1):
            for j in range(1, len(nums1) + 1):
                if nums2[i - 1] == nums1[j - 1]:  # 数组下标要减1
                    dp[i][j] = dp[i - 1][j - 1] + 1

                max_len = max(max_len, dp[i][j])

        return max_len

if __name__ == '__main__':
    nums1 = [0,1,1,1,1]
    nums2 = [1,0,1,0,1]
    print(Solution().findLength(nums1, nums2))