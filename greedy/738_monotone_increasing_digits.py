# 738. 单调递增的数字
# https://programmercarl.com/0738.%E5%8D%95%E8%B0%83%E9%80%92%E5%A2%9E%E7%9A%84%E6%95%B0%E5%AD%97.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/monotone-increasing-digits/description/

from typing import List

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if len(str(n)) == 1:
            return n
        res = list(str(n))
        i = len(res) - 1  # flag标记9开始的位置
        flag = len(res)
        while i >= 1:
            if int(res[i]) < int(res[i - 1]):  # 非递增
                res[i - 1] = str(int(res[i - 1]) - 1)
                flag = i
            i -= 1

        for i in range(flag, len(res)):
            res[i] = '9'

        return int(''.join(res).strip('0'))

if __name__ == '__main__':
    print(Solution().monotoneIncreasingDigits(100))