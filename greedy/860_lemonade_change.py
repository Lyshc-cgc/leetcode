# 860. 柠檬水找零
# https://programmercarl.com/0860.%E6%9F%A0%E6%AA%AC%E6%B0%B4%E6%89%BE%E9%9B%B6.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/lemonade-change/description/

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}
        for b in bills:
            if b == 5:
                change[5] += 1
            else:
                change[b] += 1  # 收钱
                ret_change = b - 5  # 买水
                # 先用10找
                while ret_change >= 10 and change[10] > 0:
                        change[10] -= 1
                        ret_change -= 10
                # 再用5找
                while ret_change >= 5 and change[5] > 0:
                    change[5] -= 1
                    ret_change -= 5
                if ret_change != 0:
                        return False  # 5不足以找零
        return True

if __name__ == '__main__':
    bills = [5,5,5,10,5,5,10,20,20,20]
    print(Solution().lemonadeChange(bills))
