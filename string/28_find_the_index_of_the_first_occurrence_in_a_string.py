# 28. 找出字符串中第一个匹配项的下标
# https://programmercarl.com/0028.%E5%AE%9E%E7%8E%B0strStr.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def get_next(self, pattern: str):
        next = [0] * len(pattern)
        j = 0  # common length
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = next[j - 1]
            if pattern[j] == pattern[i]:
                j += 1
            next[i] = j
        return next

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return -1
        next = self.get_next(needle)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1

if __name__ == '__main__':
    print(Solution().strStr('mississippi', 'issip'))
    print(Solution().strStr('sadbutsad', 'sad'))