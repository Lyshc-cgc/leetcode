# 383. 赎金信
# https://programmercarl.com/0383.%E8%B5%8E%E9%87%91%E4%BF%A1.html#%E6%80%9D%E8%B7%AF
# https://leetcode.cn/problems/ransom-note/description/

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_records, magazine_records = dict(), dict()
        for e in ransomNote:
            ransom_note_records[e] = ransom_note_records.get(e, 0) + 1
        for e in magazine:
            magazine_records[e] = magazine_records.get(e, 0) + 1
        flag = True
        for k, v in ransom_note_records.items():
            if v > magazine_records.get(k, 0):
                flag = False
        return flag

if __name__ == '__main__':
    print(Solution().canConstruct("a", "b"))  # False
    print(Solution().canConstruct("aa", "aab"))  # False