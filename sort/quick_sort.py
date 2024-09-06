
def partion(nums, low, high):
    # pivot = nums[low]
    # 三数中取中值
    mid = low + (high - low) // 2
    records = sorted({low: nums[low], mid: nums[mid], high: nums[high]}.items(), key=lambda x: x[-1])
    pivot_pos, pivot = records[1]
    nums[low], nums[pivot_pos] = nums[pivot_pos], nums[low]  # 交换第一个值，因为第一个值会被覆盖

    while low < high:
        while low < high and nums[high] >= pivot:  # 找比pivot小的数
            high -= 1
        if low < high:  # 只有当low<high时才交换
            nums[low] = nums[high]
            low += 1
        while low < high and nums[low] < pivot:  # 找比pivot大的数
            low += 1
        if low < high:
            nums[high] = nums[low]
            high -= 1
    # low == high
    nums[low] = pivot
    return low  # 返回枢纽位置
    
def quick_sort(nums, low, high):  # 左闭右闭
    if low < high:
        pivot_pos = partion(nums, low, high)
        quick_sort(nums, low, pivot_pos - 1)
        quick_sort(nums, pivot_pos + 1, high)

if __name__ == '__main__':
    nums = [1, 3, 28, 23, 2, 7 , 33]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)