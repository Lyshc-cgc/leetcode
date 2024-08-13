# 459.重复的子字符串
# https://programmercarl.com/0459.%E9%87%8D%E5%A4%8D%E7%9A%84%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/repeated-substring-pattern/description/

class Solution:
    def get_next(self, s):
        nxt = [0] * len(s)
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j

        return nxt

    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        巧妙的版本
        :param s:
        :return:
        """
        if len(s) == 0:
            return False
        nxt = self.get_next(s)
        if nxt[-1] != 0 and len(s) % (len(s) - nxt[-1]) == 0:  # next[-1] != 0 指字符串s有最长公共前后缀
            return True
        return False


if __name__ == '__main__':
    print(Solution().repeatedSubstringPattern("abab"))