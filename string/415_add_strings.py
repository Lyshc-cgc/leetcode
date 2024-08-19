
# 415. 字符串相加
# https://leetcode.cn/problems/add-strings/description/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        index_a, index_b = len(num1)-1, len(num2)-1
        extra = 0  # 进位
        res = ''
        while index_a > -1 and index_b > -1:
            tmp = int(num1[index_a]) + int(num2[index_b]) + extra
            res = str(tmp % 10) + res
            extra = tmp // 10
            index_a -= 1
            index_b -= 1
        while index_a > -1:
            tmp = int(num1[index_a]) + extra
            res = str(tmp % 10) + res
            extra = tmp // 10
            index_a -= 1
        while index_b > -1:
            tmp = int(num2[index_b]) + extra
            res = str(tmp % 10) + res
            extra = tmp // 10
            index_b -= 1
        if extra != 0:
            res = str(extra) +res
        return res

    def addStrings0(self, num1: str, num2: str) -> str:
        add = 0
        id1, id2 = len(num1) - 1, len(num2) - 1
        res = ''
        while id1 >= 0 or id2 >= 0 or add > 0:
            n1 = int(num1[id1]) if id1 >= 0 else 0
            n2 = int(num2[id2]) if id2 >= 0 else 0
            tmp = n1 + n2 + add
            res = str(tmp % 10) + res
            add = tmp // 10
            id1 -= 1
            id2 -= 1
        return res

if __name__ == '__main__':
    print(Solution().addStrings0('191', '9'))