from typing import List

class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def backtracing(self, s, start_idx):
        if len(self.path) == 4 and start_idx == len(s):  # 结束分割
            self.res.append('.'.join(self.path))
            return
        if start_idx >= len(s):  # 起始id超过s长度
            return

        for length in range(1, 4):  # 分割长度 1,2,3
            if len(''.join(self.path)) + (4 - len(self.path)) * 3 < len(s):  # 目前的分割方式，剩下的地址全部为3位都分不完，说明这种分割有问题，直接返回
                return
            sub_str = s[start_idx: start_idx + length]
            if len(sub_str) > 1 and sub_str.startswith('0'):  # 以0开头，无效分割，直接return
                return
            if int(sub_str) < 0 or int(sub_str) > 255:  # 数字不合格，直接返回
                return
            self.path.append(sub_str)
            self.backtracing(s, start_idx + length)  # 接下来从start_idx + length开始分割
            self.path.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.backtracing(s, 0)
        return self.res

if __name__ == '__main__':
    s = "25525511135"
    print(Solution().restoreIpAddresses(s))