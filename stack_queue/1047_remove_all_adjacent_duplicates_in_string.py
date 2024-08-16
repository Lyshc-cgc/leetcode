# 1047. 删除字符串中的所有相邻重复项
# https://programmercarl.com/1047.%E5%88%A0%E9%99%A4%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E6%89%80%E6%9C%89%E7%9B%B8%E9%82%BB%E9%87%8D%E5%A4%8D%E9%A1%B9.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/description/

from collections import deque
class Solution:
    def removeDuplicates0(self, s: str) -> str:
        """
        双指针
        :param s:
        :return:
        """
        slow, fast = 0, 1
        while 0 < fast + 1 < len(s):
            if s[slow] == s[fast]:
                s = s[:slow] + s[fast + 1:]
                if slow > 0:
                    slow -= 1
                    fast -= 1
            else:
                slow += 1
                fast += 1
        else:  # fast == len(s) - 1
            if fast < len(s) and s[slow] == s[fast]:
                s = s[:slow]
        return s

    def removeDuplicates(self, s: str) -> str:
        """
        栈
        :param s:
        :return:
        """
        stack = deque()
        for e in s:
            if len(stack) != 0 and e == stack[-1]:
                stack.pop()
            else:
                stack.append(e)
        return ''.join(stack)

if __name__ == '__main__':

    print(Solution().removeDuplicates("abbaca"))