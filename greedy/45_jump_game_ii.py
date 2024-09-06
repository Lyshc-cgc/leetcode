# 45. 跳跃游戏 II
# https://programmercarl.com/0045.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8FII.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/jump-game-ii/description/

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:

        count = 0
        if len(nums) == 1:
            return count
        pre_distance, cur_distance = 0, 0
        for i in range(len(nums)):
            cur_distance = max(i + nums[i], cur_distance)  # 更新当前可以去的最远距离
            if i == pre_distance:  # 此时位于上一次cover的最远距离，最大化利用cover
                count += 1  # 走一步,以更新cover
                pre_distance = cur_distance
                if cur_distance >= len(nums) - 1:  # 当前的cover可以覆盖目标位置
                    break
        return count

