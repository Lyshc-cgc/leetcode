# 763. 划分字母区间
# https://programmercarl.com/0763.%E5%88%92%E5%88%86%E5%AD%97%E6%AF%8D%E5%8C%BA%E9%97%B4.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/partition-labels/description/

from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        records = dict()
        for i in range(len(s)):
            ch = s[i]
            if ch not in records:
                records[ch] = {}
                records[ch]['start'] = i  # 初次出现记录起始位置,
                records[ch]['end'] = i
            else:
                records[ch]['end'] = i  # 多次出现记录结束位置，右闭

        records = [(v['start'], v['end']) for k, v in records.items()]
        records = sorted(records, key=lambda x: x[0])  # 按起始位置排序

        res = []
        left = 0
        right = 0  # 记录cover的右边界
        for i in range(len(records)):
            if records[i][0] > right:  # 没和前面的cover挨着
                res.append(right - left + 1)
                left = records[i][0]
                right = records[i][1]
            else:
                right = max(records[i][1], right)  # cover长度不断向右扩展

        res.append(right - left + 1)  # 最后一个
        return res

if __name__ == '__main__':
    s = "eccbbbbdec"
    print(Solution().partitionLabels(s))