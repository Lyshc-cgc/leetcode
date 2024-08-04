# 面试题 02.07. 链表相交
# https://programmercarl.com/%E9%9D%A2%E8%AF%95%E9%A2%9802.07.%E9%93%BE%E8%A1%A8%E7%9B%B8%E4%BA%A4.html
# https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/description/

from typing import Optional
from utils import linked_list_util
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def get_length(self, head):
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a_len, b_len = self.get_length(headA), self.get_length(headB)
        # 让短链表与长链表的长度从尾结点开始对齐
        if a_len > b_len:  # a长，移动a的头结点
            move_len = a_len - b_len
            while move_len:  # while move_len > 0:
                headA = headA.next
                move_len -= 1
        else:
            move_len = b_len - a_len  # b
            while move_len:
                headB = headB.next
                move_len -= 1
        index_a, index_b = headA, headB
        while not index_a == index_b:  # 地址不相等，同时前进
            index_a = index_a.next
            index_b = index_b.next
        return index_a

if __name__ == '__main__':
    intersectVal = 8
    nums_a = [4,1,8,4,5]
    nums_b = [5,0,1,8,4,5]
    head_a = linked_list_util.init_lined_list(nums_a)
    head_b = linked_list_util.init_lined_list(nums_b)
    linked_list_util.print_linked_list(head_a)
    print('---------')
    linked_list_util.print_linked_list(head_b)
    print('---------')
    linked_list_util.print_linked_list(Solution().getIntersectionNode(head_a, head_b))