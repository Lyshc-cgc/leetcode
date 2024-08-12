# 541. 反转字符串 II
# https://programmercarl.com/0541.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2II.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/reverse-string-ii/description/
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        start = 0
        res_str = ''
        while start < len(s):
            sub_str = s[start: start + 2*k]
            reverse_str = list(sub_str[: k])
            left, right = 0, len(reverse_str) - 1
            while left < right:
                reverse_str[left], reverse_str[right] = reverse_str[right], reverse_str[left]
                left += 1
                right -= 1
            res_str += ''.join(reverse_str) + sub_str[k:]
            start += 2*k
        return res_str

if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    print(Solution().reverseStr(s, k))