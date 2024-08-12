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

if __name__ == '__main__':
    s = "the sky is blue"
    print(Solution().reverseWords(s))  # "blue is sky the"
    s = "  hello world  "
    print(Solution().reverseWords(s))  # "world hello"
    s = "a good    example"
    print(Solution().reverseWords(s))  # "example good a"