# 150. 逆波兰表达式求值
# https://programmercarl.com/0150.%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B1%82%E5%80%BC.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/evaluate-reverse-polish-notation/description/

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opearations = {'+', '-', '*', '/'}
        for t in tokens:
            if t in opearations:
                num_1 = int(stack.pop())
                num_0 = int(stack.pop())  # 第一个操作数第二个出栈
                if t == '+':
                    res = num_0 + num_1
                elif t == '-':
                    res = num_0 - num_1
                elif t == '*':
                    res = num_0 * num_1
                elif t == '/':
                    if num_0 * num_1 > 0:  # 都为正，或都为负
                        res = num_0 // num_1
                    else:
                        res = abs(num_0) // abs(num_1) * -1
                stack.append(res)
            else:
                stack.append(int(t))
        return stack.pop()


if __name__ == '__main__':
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(Solution().evalRPN(tokens))