# 96. 不同的二叉搜索树
# https://programmercarl.com/0096.%E4%B8%8D%E5%90%8C%E7%9A%84%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/unique-binary-search-trees/description/

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        # dp[1] = 1
        for i in range(1, n + 1):
            for j in range(i):
                # 如 dp[3] = dp[0] * dp[2] + dp[1] * dp[1] + dp[2] * dp[0]
                # 当根节点为1时，左边0个节点，右边2个节点
                # 当根节点为2时，左边1个，右边1个
                # ....3..., 左边2个，右边0个
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[-1]

if __name__ == '__main__':
    print(Solution().numTrees(3))
