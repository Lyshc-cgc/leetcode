# 202. 快乐数
# https://programmercarl.com/0202.%E5%BF%AB%E4%B9%90%E6%95%B0.html#%E6%80%9D%E8%B7%AF
# https://leetcode.cn/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()  # 已出现的数字
        while n != 1:
            number = 0
            while n:
                number += (n % 10) ** 2
                n //= 10
            if number in nums:  # 陷入循环
                return False
            else:
                nums.add(number)
                n = number
        return True

if __name__ == '__main__':
    print(Solution().isHappy(19))  # True