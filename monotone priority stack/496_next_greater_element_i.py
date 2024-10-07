# 496. 下一个更大元素 I
# https://programmercarl.com/0496.%E4%B8%8B%E4%B8%80%E4%B8%AA%E6%9B%B4%E5%A4%A7%E5%85%83%E7%B4%A0I.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/next-greater-element-i/description/

from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1. 记录nums2中每个元素的下一个更大元素的位置
        nxt_greater_nums2 = [-1] * len(nums2)
        stack = []  # 递增栈
        for i in range(len(nums2)):
            if len(stack) == 0 or nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) and nums2[i] > nums2[stack[-1]]:
                    # i指示元素，为 stack[-1]指示元素右侧第一个比他大的
                    top = stack.pop()
                    nxt_greater_nums2[top] = i  # top元素下一个更大元素在位置i
                stack.append(i)

        # 2. 为nums1每个元素检索其在nums2中下一个最大元素
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            if nxt_greater_nums2[idx] != -1:
                res[i] = nums2[nxt_greater_nums2[idx]]  # nxt_greater_nums2[idx]是最大元素位置
        return res

if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(Solution().nextGreaterElement(nums1, nums2))