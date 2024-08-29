
def insertion_sort(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            tmp = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > tmp:
                nums[j + 1] = nums[j]
                j -= 1
            # 此时要么j为-1，要么 nums[j] <= tmp
            nums[j + 1] = tmp
    return nums

if __name__ == '__main__':
    print(insertion_sort([1, 3, 28, 23, 2]))