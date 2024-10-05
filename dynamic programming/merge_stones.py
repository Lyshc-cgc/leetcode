# 区间dp
# https://blog.csdn.net/qq_42581685/article/details/122261230

def main(N, stones):
    prefix_sum = [0] * (N + 1)  # 前缀和
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + stones[i - 1]
    # prefix_sum.append(acc)  # 此时sum[i,j] 为s[i] + s[i + 1]+..+s[j] = sum[j + 1] - sum[i]
    dp = [[float('inf')] * N for _ in range(N)]  # dp[i][j]表示合并stones[i:j + 1]所付出的最少代价
    for i in range(N):
        dp[i][i] = 0

    for length in range(2, N + 1):  # 遍历区间长度
        for i in range(0, N - length + 1):  # 遍历起点
            j = i + length - 1  # 结束位置（闭区间）
            for k in range(i, j):  # 分割点
                dp[i][j] = min(dp[i][k] + dp[k+1][j] + prefix_sum[j + 1] - prefix_sum[i], dp[i][j])
    print(dp[0][-1])
    # print(max_dp[0][-1])

# 环状dp
# https://www.luogu.com.cn/problem/P1880
def main0(N, stones):
    stones += stones  # 破环成链
    prefix_sum = [0] * (2 * N + 1)  # 前缀和
    for i in range(1, 2 * N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + stones[i - 1]

    # prefix_sum.append(acc)  # 此时sum[i,j] 为s[i] + s[i + 1]+..+s[j] = sum[j + 1] - sum[i]
    min_dp = [[float('inf')] * N * 2 for _ in range(N * 2)]  # dp[i][j]表示合并stones[i:j + 1]所付出的最少代价
    max_dp = [[float('-inf')] * N * 2 for _ in range(N * 2)]  # dp[i][j]表示合并stones[i:j + 1]所付出的最多代价

    for i in range(2 * N):
        min_dp[i][i] = 0
        max_dp[i][i] = 0
    # 起点从0开始到N-1的位置
    for length in range(2, N + 1):  # 遍历区间长度
        for i in range(0, 2 * N - length + 1):  # 遍历起点
            j = i + length - 1  # 结束位置（闭区间）
            for k in range(i, j):  # 分割点
                min_dp[i][j] = min(min_dp[i][k] + min_dp[k + 1][j] + prefix_sum[j + 1] - prefix_sum[i], min_dp[i][j])
                max_dp[i][j] = max(max_dp[i][k] + max_dp[k + 1][j] + prefix_sum[j + 1] - prefix_sum[i], max_dp[i][j])

    # 计算不同起点的链的结果
    min_res, max_res = float('inf'), float('-inf')
    for start in range(N):
        min_res = min(min_res, min_dp[start][start + N - 1])
        max_res = max(max_res, max_dp[start][start + N - 1])
    print(min_res)
    print(max_res)

if __name__ == '__main__':
    N = int(input().strip())
    stones = list(map(int, input().strip().split()))
    main0(N, stones)