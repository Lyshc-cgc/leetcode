# 704. 二分查找
# https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html
# https://leetcode.cn/problems/binary-search/description/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while(left <= right):
            middle = left + (right - left) //2
            if (nums[middle] < target):  # 右半区
                left = middle + 1
            elif (nums[middle] > target):  # 左半区
                right = middle - 1
            else:
                return middle
        else:
            return -1

if __name__ == '__main__':
    solution = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    print(solution.search(nums, target))