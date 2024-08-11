# 18. 四数之和
# https://programmercarl.com/0018.%E5%9B%9B%E6%95%B0%E4%B9%8B%E5%92%8C.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/4sum/description/

from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        if len(nums) < 4:
            return res
        for i in range(len(nums)):
            if target > 0 and nums[i] > target:
                break
            if i > 0 and nums[i] == nums[i-1]:  # 1级剪枝
                continue
            for j in range(i+1, len(nums)):
                left, right = j+1, len(nums)-1
                if target > 0  and nums[i] + nums[j] > target:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res

if __name__ == '__main__':
    print(Solution().fourSum([1,0,-1,0,-2,2], 0))  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    print(Solution().fourSum([2,2,2,2,2], 8))  # [[2,2,2,2]]
    print(Solution().fourSum([0,0,0,0], 0))  # [[0,0,0,0]]