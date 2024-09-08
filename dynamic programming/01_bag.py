# https://kamacoder.com/problempage.php?pid=1046
# https://programmercarl.com/%E8%83%8C%E5%8C%85%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%8001%E8%83%8C%E5%8C%85-1.html#%E6%80%9D%E8%B7%AF

def bag(values, weights, M, N):
    dp = [[0] * (N + 1) for _ in range(M)]  # dp[i][j]表示从[0,i]中选择物品，放进容量为j的背包里，价值总和最大值

    # 1.初始化
    for j in range(N + 1):  # 0不要
        if j < weights[0]:  # 当容量小于第一物品的重量时，为0
            dp[0][j] = 0
        else:  # 容量大于等于第一物品的重量时，此时背包可选物品为weights[0],最大价值为values[0]
            dp[0][j] = values[0]

    # 2.遍历
    for i in range(1, M):  # 外层遍历物品
        for j in range(N + 1):  # 内层遍历容量
            if j < weights[i]:  # 无法放第i个物品
                dp[i][j] = dp[i - 1][j]  # 直接沿用dp[i - 1][j]的结果
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])

    print(dp[M - 1][N])



if __name__ == '__main__':
    M, N = map(int, input().strip().split())
    weights = list(map(int, input().strip().split()))
    values = list(map(int, input().strip().split()))
    bag(values, weights, M, N)