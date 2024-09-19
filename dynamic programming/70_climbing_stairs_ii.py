# https://programmercarl.com/0070.%E7%88%AC%E6%A5%BC%E6%A2%AF%E5%AE%8C%E5%85%A8%E8%83%8C%E5%8C%85%E7%89%88%E6%9C%AC.html#%E6%80%9D%E8%B7%AF
# https://kamacoder.com/problempage.php?pid=1067

def climbing_stairs(n, m):
    dp = [0] * (n + 1)
    dp[0] = 1
    # 组合数
    # 外围遍历容量，内层遍历物体
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if j >= i:
                dp[j] += dp[j - i]
    return dp[-1]

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    print(climbing_stairs(n, m))


