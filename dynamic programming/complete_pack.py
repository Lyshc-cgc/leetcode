# 完全背包问题
# https://kamacoder.com/problempage.php?pid=1052
# https://programmercarl.com/%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80%E5%AE%8C%E5%85%A8%E8%83%8C%E5%8C%85.html#%E6%80%9D%E8%B7%AF

def complete_pack(W, V, N):
    """

    :param W: 各物品重量
    :param V: 各物品价值
    :param N: 背包总重量
    :return:
    """
    dp = [0] * (N + 1)
    for i in range(len(W)):
        for j in range(1, N + 1):
            if j >= W[i]:
                dp[j] = max(dp[j], dp[j - W[i]] + V[i])
    return dp[-1]

if __name__ == '__main__':
    count, N = map(int, input().split())
    W, V = [], []
    for _ in range(count):
        wi, vi = map(int, input().split())
        W.append(wi)
        V.append(vi)
    print(complete_pack(W, V, N))



