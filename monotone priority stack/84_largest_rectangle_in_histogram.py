# 84. 柱状图中最大的矩形
# https://programmercarl.com/0084.%E6%9F%B1%E7%8A%B6%E5%9B%BE%E4%B8%AD%E6%9C%80%E5%A4%A7%E7%9A%84%E7%9F%A9%E5%BD%A2.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/largest-rectangle-in-histogram/description/

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0, 0) # 前后放一个0，防止错过heights数组非递增而错过计算矩形面积
        heights.append(0)
        stack = [0]  # 单调栈，栈顶到栈底递减. 先把heights首添加的0放进去
        max_rectangle = 0
        for i in range(1, len(heights)):
            max_rectangle = max(max_rectangle, heights[i] * 1)  # 先比较第i根柱子本身
            if len(stack) == 0 or heights[i] > heights[stack[-1]]:
                stack.append(i)
            elif heights[i] == heights[stack[-1]]:
                stack.pop()
                stack.append(i)  # 用最新的替换掉
            else:
                # 相邻的柱子组成的矩形，使用mid和top指向的两根柱子
                while len(stack) and heights[i] < heights[stack[-1]]:
                    mid = stack.pop()  # 当前最高的柱子
                    if len(stack):
                        top = stack[-1]  # mid左边最高的柱子.这里不能pop，柱子需要保留作为下一次的mid
                        h = heights[mid]
                        w = i - top - 1  # 宽度
                        max_rectangle = max(max_rectangle, h * w)
                stack.append(i)

        return max_rectangle


if __name__ == '__main__':
    heights = [1, 1]
    print(Solution().largestRectangleArea0(heights))