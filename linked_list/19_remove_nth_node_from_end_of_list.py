# 19. 删除链表的倒数第 N 个结点
# https://programmercarl.com/0019.%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E8%8A%82%E7%82%B9.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/

from typing import Optional
from utils import linked_list_util
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        双指针法
        :param head:
        :param n:
        :return:
        """
        dummy_head = ListNode(0, head)
        # 快指针先走n步
        fast, fast_index = dummy_head, n
        while fast.next and fast_index > 0:
            fast = fast.next
            fast_index -= 1
        if fast_index > 0 :  # fast已经指到尾结点了， 但是fast_index还大，说明n超出了链表大小
            return
        slow = dummy_head
        while fast.next:
            fast = fast.next
            slow = slow.next
        # 当fast指向尾结点时，slow指向待删除节点的上一个
        slow.next = slow.next.next  # 删除
        return dummy_head.next

if __name__ == '__main__':
    nums = [1, 2]
    head = linked_list_util.init_lined_list(nums)
    linked_list_util.print_linked_list(head)
    print('-------')
    linked_list_util.print_linked_list(Solution().removeNthFromEnd(head,1))