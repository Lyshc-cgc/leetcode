# 55. 跳跃游戏
# https://www.programmercarl.com/0055.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8F.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/jump-game/description/

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        cover = 0
        i = 0
        while i <= cover:
            if cover >= len(nums) - 1:
                return True
            cover = max(i + nums[i], cover)  # 更新覆盖范围
            i += 1
        return False