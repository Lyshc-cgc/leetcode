# 503. 下一个更大元素 II
# https://programmercarl.com/0503.%E4%B8%8B%E4%B8%80%E4%B8%AA%E6%9B%B4%E5%A4%A7%E5%85%83%E7%B4%A0II.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/next-greater-element-ii/description/

from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        original_len = len(nums)
        nums += nums
        stack = []  # 从栈顶到栈低 递增
        res = [-1] * len(nums)  # res[i]表示第i个元素下一个更大元素的值
        for i in range(len(nums) - 1):
            if len(stack) == 0 or nums[i] < nums[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) and nums[i] > nums[stack[-1]]:
                    top = stack.pop()
                    res[top] = nums[i]
                stack.append(i)
        return res[:original_len]

if __name__ == '__main__':
    nums = [1,2,3,4,3]
    print(Solution().nextGreaterElements(nums))
