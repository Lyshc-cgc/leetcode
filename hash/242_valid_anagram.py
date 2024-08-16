# 242. 有效的字母异位词
# https://programmercarl.com/0242.%E6%9C%89%E6%95%88%E7%9A%84%E5%AD%97%E6%AF%8D%E5%BC%82%E4%BD%8D%E8%AF%8D.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        for e in s:
            if e in s_dict:
                s_dict[e] += 1
            else:
                s_dict[e] = 1
        t_dict = dict()
        for e in t:
            if e in t_dict:
                t_dict[e] += 1
            else:
                t_dict[e] = 1
        return s_dict == t_dict

    def isAnagram1(self, s: str, t: str) -> bool:
        counter_s, counter_t = dict(), dict()
        for e in s:
            counter_s[e] = counter_s.get(e, 0) + 1
        for e in t:
            counter_t[e] = counter_t.get(e, 0) + 1
        return counter_s == counter_t

if __name__ == '__main__':
    print(Solution().isAnagram1("anagram", "nagaram"))  # True