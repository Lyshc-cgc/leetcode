# 42. 接雨水
# https://programmercarl.com/0042.%E6%8E%A5%E9%9B%A8%E6%B0%B4.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/trapping-rain-water/description/

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        单调栈
        """
        stack = []  # 栈顶到栈底递增
        volume = 0
        for i in range(len(height)):
            if i == 0 or height[i] < height[stack[-1]]:
                stack.append(i)
            elif height[i] == height[stack[-1]]:  # 替换掉
                stack.pop()
                stack.append(i)
            else:
                while len(stack) and height[i] > height[stack[-1]]:
                    # 接住雨水
                    mid = stack.pop()  # 凹槽位置
                    # height[stack[-1]] 左边柱子，height[i]为右边柱子
                    if len(stack):  # 如果为空，就无法形成一个凹槽
                        top = stack[-1]  # 这里不能Pop，每次接了雨水后，原来的top位置就是新的底部位置了
                        h = min(height[top], height[i]) - height[mid]
                        w = i - top - 1
                        volume += h * w
                stack.append(i)
        return volume

    def trap0(self, height: List[int]) -> int:
        """
        双指针
        :param height:
        :return:
        """
        max_left = [0] * len(height)  # 每个位置上左边的最大高度
        max_right = [0] * len(height)  # 每个位置上右边的最大高度
        max_left[0] = height[0]
        for i in range(1, len(height)):
            max_left[i] = max(height[i], max_left[i - 1])
        max_right[-1] = height[-1]
        j = len(height) - 2
        while j >= 0:
            max_right[j] = max(height[j], max_right[j + 1])
            j -= 1
        volume = 0
        for i in range(len(height)):
            h = min(max_left[i], max_right[i]) - height[i]
            if h > 0:
                volume += h
        return volume

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(height))
