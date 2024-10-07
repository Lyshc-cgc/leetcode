# 215. 数组中的第K个最大元素
# https://leetcode.cn/problems/kth-largest-element-in-an-array/description/
import random
from typing import List

class Solution:
    def partion(self, nums, left, right):
        """
        左闭右闭
        :param nums:
        :param left:
        :param right:
        :return:
        """
        mid = left + (right - left) // 2
        records = {left:nums[left], right:nums[right], mid:nums[mid]}
        pivot_idx, pivot = sorted(records.items(), key=lambda x: x[-1])[1]
        nums[left], nums[pivot_idx] = nums[pivot_idx], nums[left]
        pivot = nums[left]

        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            if left < right:
                nums[left] = nums[right]
                left += 1
            while left < right and nums[left] <= pivot:
                left += 1
            if left < right:
                nums[right] = nums[left]
                right -= 1

        # 此时left == right,安放pivot
        nums[left] = pivot
        return left

    def quick_sort_with_k(self, k, nums, left, right):
        if left < right:
            pivot = self.partion(nums, left, right)
            if pivot == len(nums) - k:
                return nums[pivot]
            if len(nums) - pivot < k:  # 当pivot右边的不足k个时，才对左边进行排序
                left_zone = self.quick_sort_with_k(k, nums, left, pivot - 1)
                if left_zone:
                    return left_zone
            right_zone = self.quick_sort_with_k(k, nums, pivot + 1, right)
            if right_zone:
                return right_zone
        return None

    def findKthLargest0(self, nums: List[int], k: int) -> int:
        res = self.quick_sort_with_k(k, nums, 0 , len(nums) - 1)
        if res:
            return res
        else:
            return nums[-k]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickfind(nums, k):
            idx = random.randint(0, len(nums) - 1)
            pivot = nums[idx]
            left = [n for n in nums if n > pivot]
            if len(left) >= k:  # 说明第k大的元素在left中
                return quickfind(left, k)

            k -= len(left)  # k缩小，减掉len(left)
            eqs = [n for n in nums if n == pivot]  # 所有与pivot相等的元素
            if len(eqs) >= k:  # 说明第k大的元素在eqs中，所有元素都相等，那么就返回pivot
                return pivot

            k -= len(eqs)
            right = [n for n in nums if n < pivot]
            return quickfind(right, k)
        return quickfind(nums, k)


if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    print(Solution().findKthLargest(nums, 2))
