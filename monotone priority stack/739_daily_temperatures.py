# 739. 每日温度
# https://programmercarl.com/0739.%E6%AF%8F%E6%97%A5%E6%B8%A9%E5%BA%A6.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/daily-temperatures/description/

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # 维护一个单调递减的栈
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if len(stack) == 0 or temperatures[i] <= temperatures[stack[-1]]:  # 小于等于栈顶指示元素则入栈
                stack.append(i)
            else:
                while len(stack) and temperatures[i] > temperatures[stack[-1]]:
                    # 此时i指示的元素，为栈顶所指示元素右边第一个比他大的
                    top = stack.pop()
                    res[top] = i - top  # i - top为相隔距离
                stack.append(i)
        return res

if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(temperatures))