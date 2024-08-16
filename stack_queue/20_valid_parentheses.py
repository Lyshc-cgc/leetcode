# 20. 有效的括号
# https://programmercarl.com/0020.%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/valid-parentheses/description/

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        mapping = {'{': '}', '[': ']', '(': ')'}
        for e in s:
            if e in mapping.keys():
                q.append(e)
            else:
                if len(q) == 0:
                    return False
                tmp = q.pop()
                if mapping[tmp] != e:
                    return False
        if len(q) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    s = "([)]"
    print(Solution().isValid(s))