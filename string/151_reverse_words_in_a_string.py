# 151. 反转字符串中的单词
# https://programmercarl.com/0151.%E7%BF%BB%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2%E9%87%8C%E7%9A%84%E5%8D%95%E8%AF%8D.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/reverse-words-in-a-string/description/

class Solution:
    def reverseWords(self, s: str) -> str:

        slow, fast = 0, 0
        res = ''
        while fast < len(s):
            if s[fast] == ' ' and s[slow] == ' ':  # 处理多个空格
                fast += 1
                slow += 1
            elif s[fast] == ' ' and s[slow] != ' ':
                res = ' ' + s[slow: fast] + res
                fast += 1
                slow = fast
            else:
                fast += 1
        if fast != slow:  # 处理最后一个单词
            res = ' ' + s[slow: fast]  + res
        return res[1:]  # 去掉第一个空格

    def reverse(self, s, start, end):  # 左闭右闭
        l, r = start, end
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s
    def reverseWords0(self, s):
        s = list(s)
        # 清除多余空格
        slow, fast = 0, 0
        while fast < len(s):
            if s[fast] != ' ':
                s[slow] = s[fast]
                slow += 1
                fast += 1
            else:  # s[fast] == ' '
                if slow != 0:
                    s[slow] = ' '  # 手动加一个空格
                    slow += 1
                while fast < len(s) and s[fast] == ' ':
                    fast += 1
        if s[-1] == ' ':
            s = s[:slow - 1]  # s最后有个空格
        else:
            s = s[:slow]
        s = self.reverse(s, 0, len(s) - 1)
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                s = self.reverse(s, start, i - 1)
                start = i + 1
        s = self.reverse(s, start, len(s) - 1)

        return ''.join(s)

if __name__ == '__main__':
    s = "the sky is blue"
    print(Solution().reverseWords(s))  # "blue is sky the"
    s = "  hello world  "
    print(Solution().reverseWords(s))  # "world hello"
    s = "a good    example"
    print(Solution().reverseWords(s))  # "example good a"