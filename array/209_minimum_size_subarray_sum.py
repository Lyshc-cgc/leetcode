# 209. 长度最小的子数组
# https://programmercarl.com/0209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.html
# https://leetcode.cn/problems/minimum-size-subarray-sum/description/
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        滑动窗口法
        :param target:
        :param nums:
        :return:
        """
        start = 0  # 滑动窗口起始位置
        min_size = 1000000  # 滑动窗口最小长度
        window_sum = 0
        for end in range(len(nums)):
            window_sum += nums[end]
            while window_sum >= target:  # 当window中各数之和大于等于target，记录目前窗口状态并则尝试缩小窗口
                window_size = end - start + 1
                if window_size < min_size:
                    min_size = window_size
                # 缩小窗口
                window_sum -= nums[start]
                start += 1
        if min_size == 1000000:
            return 0
        return min_size


if __name__ == '__main__':
    nums = [2,3,1,2,4,3]
    target = 7
    print(Solution().minSubArrayLen(target, nums))