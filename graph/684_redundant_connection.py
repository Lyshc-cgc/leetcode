# 684. 冗余连接
# https://programmercarl.com/0684.%E5%86%97%E4%BD%99%E8%BF%9E%E6%8E%A5.html#%E6%80%9D%E8%B7%AF
# https://leetcode.cn/problems/redundant-connection/description/

from typing import List

class Solution:
    def __init__(self):
        self.father = None  # 父节点集合

    def init_father(self, n):
        self.father = [i for i in range(n)]  # 每个节点初始的父节点为自身

    def find(self, tgt):
        """
        寻找tgt的根节点
        :param tgt:
        :return:
        """
        if tgt == self.father[tgt]:  # 父节点为自身，此时为根节点
            return tgt
        else:
            # 路径压缩
            self.father[tgt] = self.find(self.father[tgt])  # 根节点作为父节点
            return self.father[tgt]

    def is_same(self, u, v):
        """
        判断是否是同一个根节点
        :param u:
        :param v:
        :return:
        """
        return self.find(u) == self.find(v)

    def merge(self, u, v):
        """
        将 u -> v这条边加入并查集
        :param u:
        :param v:
        :return:
        """
        u = self.find(u)  # 寻找u的根
        v = self.find(v)  # 寻找v的根
        if u == v:  # 如果根相同
            return
        self.father[u] = v

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.init_father(1005)
        redant_edges = []
        for e in edges:
            if self.is_same(e[0], e[1]):  # 冗余了
                redant_edges.append(e)
            else:
                self.merge(e[0], e[1])
        return redant_edges[-1]