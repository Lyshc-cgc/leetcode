# 15. 三数之和
# https://programmercarl.com/0015.%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/3sum/description/

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        求解思路是先排序，然后固定一个数，另外两个数用双指针法找到
        :param nums:
        :return:
        """
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:  # 三元组中最小的数大于0，和不可能为0
                return res
            left, right = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:  # 当nums[i]定死时，会把另外两个数的组合找出来，所以nums[i]重复时，会重复找到相同的组合
                continue
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                    left += 1
        return res

if __name__ == '__main__':
    # print(Solution().threeSum([-1,0,1,2,-1,-4]))  # [[-1, -1, 2], [-1, 0, 1]]
    print(Solution().threeSum([0,0,0]))  # [[0,0,0]]