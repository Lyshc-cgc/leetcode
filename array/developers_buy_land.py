# 44. 开发商购买土地
# https://programmercarl.com/kamacoder/0044.%E5%BC%80%E5%8F%91%E5%95%86%E8%B4%AD%E4%B9%B0%E5%9C%9F%E5%9C%B0.html#%E6%80%9D%E8%B7%AF
# https://kamacoder.com/problempage.php?pid=1044

def main():
    n, m = map(int, input().strip().split())
    lands = []
    for i in range(n):
        lands.append(list(map(int, input().strip().split())))

    # 计算每行的前缀和
    row_sums = [0] * n
    for i in range(n):
        row_sum = 0
        for j in range(m):
            row_sum += lands[i][j]
        row_sums[i] = row_sum

    # 计算每列的前缀和
    col_sums = [0] * m
    for j in range(m):
        col_sum = 0
        for i in range(n):
            col_sum += lands[i][j]
        col_sums[j] = col_sum

    all_sum = sum(row_sums)  # 总和，sum(col_sums)
    # 土地划分
    min_difference = float('inf')

    # 横着化
    value = 0   # 将第i行及其之前的化给一个公司，其所得土地价值是一个前缀和
    for i in range(n):
        value += row_sums[i]
        min_difference = min(min_difference, abs(all_sum - 2 * value))  # all_sum - value是令一个公司所得价值，再减value就是两者价值之差

    # 竖着化
    value = 0
    for j in range(m):
        value += col_sums[j]
        min_difference = min(min_difference, abs(all_sum - 2 * value))
    print(min_difference)

if __name__ == '__main__':
    main()