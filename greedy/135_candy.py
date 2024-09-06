# 135. 分发糖果
# https://programmercarl.com/0135.%E5%88%86%E5%8F%91%E7%B3%96%E6%9E%9C.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/candy/description/

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        # 从左到右.保证右边的孩子评分高就一定比左边的多
        for idx in range(1, len(ratings)):  # 从1开始，每个元素比较前一个元素
            if ratings[idx] > ratings[idx - 1]:  # 右孩子评分高
                candies[idx] = candies[idx - 1] + 1  # 在前一个人的基础上+1

        # 从右到左。保证左孩子高评分的分更多糖果
        idx = len(ratings) - 1
        while idx:
            if ratings[idx] < ratings[idx - 1]:  # 左孩子评分高
                # candies[idx] + 1 是比右孩子多的糖果
                # candies[idx - 1]里面保存的是比左孩子多的糖果
                candies[idx - 1] = max(candies[idx] + 1, candies[idx - 1])  # 保证左孩子的糖果比右边的多，且还要比左边的多
            idx -= 1
        return sum(candies)

if __name__ == '__main__':
    print(Solution().candy([1,6,10,8,7,3,2]))

