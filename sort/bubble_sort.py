def bubble_sort(nums):
    for i in range(0, len(nums)):
        for j in range(1, len(nums) - i):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]  #交换位置
    return nums

if __name__ == '__main__':
    print(bubble_sort([1, 3, 28, 23, 2]))