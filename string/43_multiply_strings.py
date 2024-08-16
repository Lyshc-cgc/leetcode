# 43. 字符串相乘
# https://leetcode.cn/problems/multiply-strings/description/

class Solution:
    def stradd(self, num1: str, num2: str):
        index_a, index_b = len(num1) - 1, len(num2) - 1
        extra = 0
        res = []
        while index_a >= 0 or index_b >= 0 or extra != 0:
            x = int(num1[index_a]) if index_a >= 0 else 0
            y = int(num2[index_b]) if index_b >= 0 else 0
            tmp = x + y + extra
            res.append(str(tmp % 10))
            extra = tmp // 10
            index_a -= 1
            index_b -= 1
        return ''.join(res[::-1])

    def str2num(self, string: str):
        num = 0
        for e in string:
            num = num * 10 + int(e)
        return num

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        if len(num1) < 6 and len(num2) < 6:
            return str(self.str2num(num1) * self.str2num(num2))
        else:
            mid1, mid2 = len(num1)//2, len(num2)//2
            a, b = num1[: mid1], num1[mid1:]  # num1 = a * 10 ** mid1+ b
            c, d = num2[: mid2], num2[mid2:]  # num2 = c * 10 ** mid2+ d
            ac = self.multiply(a, c) + '0' * (len(num1) - mid1 + len(num2) - mid2)
            ad = self.multiply(a, d) + '0' * (len(num1) - mid1)
            bc = self.multiply(b, c) + '0' * (len(num2) - mid2)
            bd = self.multiply(b, d)
            return self.stradd(self.stradd(ac, ad), self.stradd(bc, bd))

if __name__ == '__main__':
    print(Solution().multiply('2', '30'))