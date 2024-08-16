# 142. 环形链表 II
# https://programmercarl.com/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/linked-list-cycle-ii/description/

from typing import Optional
from utils import linked_list_util

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        fast = slow = head
        # 快慢指针同时移动，找到相遇节点
        while slow.next and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return  # 无环
        # 头结点定义一个指针，相遇节点定义一个指针，然后同时开始向前移动（一个格子）
        index0, index1 = head, fast
        while index0 != index1:
            index0 = index0.next
            index1 = index1.next

        return index0

    def detectCycle1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        seen = set()
        current = head
        while current:
            if current in seen:
                return current
            else:
                seen.add(current)
            current = current.next
        return None
