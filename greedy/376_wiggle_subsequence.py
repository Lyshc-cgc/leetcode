# 376. 摆动序列
# https://programmercarl.com/0376.%E6%91%86%E5%8A%A8%E5%BA%8F%E5%88%97.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/wiggle-subsequence/description/

from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        count = 1  # 默认最右边有一个峰值
        pre_dif = 0
        for i in range(len(nums) - 1):
            cur_dif = nums[i + 1] - nums[i]
            if pre_dif <= 0 and cur_dif > 0 or pre_dif >= 0 and cur_dif < 0:
                count += 1
                pre_dif = cur_dif  # 记录当前坡度
        return count
if __name__ == '__main__':
    nums = [1,17,5,10,13,15,10,5,16,8]
    print(Solution().wiggleMaxLength(nums))