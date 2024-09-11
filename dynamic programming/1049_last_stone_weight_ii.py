# 1049. 最后一块石头的重量 II
# https://programmercarl.com/1049.%E6%9C%80%E5%90%8E%E4%B8%80%E5%9D%97%E7%9F%B3%E5%A4%B4%E7%9A%84%E9%87%8D%E9%87%8FII.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/last-stone-weight-ii/description/

from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 尽量分成重量相等的两堆
        tgt = sum(stones) // 2
        dp = [0] * (tgt + 1)  # dp[tgt]表示容量为tgt时能放得最多石头重量
        # 类似LC416 https://leetcode.cn/problems/partition-equal-subset-sum/description/
        for i in range(len(stones)):
            j = tgt
            while j >= stones[i]:
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
                j -= 1
        # 一堆是dp[tgt]，另一堆sum(stones) - dp[tgt]
        a, b = dp[tgt], sum(stones) - dp[tgt]
        return abs(a - b)

if __name__ == '__main__':
    stones = [31,26,33,21,40]
    print(Solution().lastStoneWeightII(stones))