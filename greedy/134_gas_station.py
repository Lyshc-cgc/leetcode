# 134. 加油站
# https://programmercarl.com/0134.%E5%8A%A0%E6%B2%B9%E7%AB%99.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/gas-station/description/

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remain = [g - c for g, c in zip(gas, cost)]
        if sum(remain) < 0:  # 不可能绕一周的
            return -1

        # 到这里一定可以绕一周
        oil_box = 0  # 记录油箱中的油
        start_idx = 0  # 默认从0开始
        for idx in range(len(remain)):
            oil_box += remain[idx]
            if oil_box < 0:
                start_idx = (idx + 1) % len(remain)  # 当前起始位置开始到目前，油箱为负。不能跑到这里。因此从下一个开始
                oil_box = 0

        return start_idx

if __name__ == '__main__':
    gas = [5,1,2,3,4]
    cost = [4,4,1,5,1]
    print(Solution().canCompleteCircuit(gas, cost))