# 206. 反转链表
# https://programmercarl.com/0206.%E7%BF%BB%E8%BD%AC%E9%93%BE%E8%A1%A8.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/reverse-linked-list/description/

from typing import Optional
from utils import linked_list_util

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def reverseList1(self, head: Optional[ListNode], pre_node) -> Optional[ListNode]:
        """
        找到尾结点后，反向依次反转指针
        :param head:
        :param pre_node:
        :return:
        """
        if not head:  # 链表为空，啥也不干
            return
        if head.next:  # 若没有到尾节点，指针往前移动，并将自身的指针作为pre_node传入
            self.reverseList1(head.next, head)
        else:  # 尾结点
            self.head = head  # 尾结点作为反转后的头结点
        # 开始反转
        head.next = pre_node
        return

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:  # 链表为空，啥也不干
            return None
        elif not head.next:  # 只有一个结点, 不用反转，直接返回
            self.head = head
            return self.head
        tail = self.reverse(head)  # 反转
        tail.next = None
        return self.head

    def reverse(self, current):
        if current.next.next:  # 下一个节点不为尾结点，则指针前移
            self.reverse(current.next)
        else:
            self.head = current.next  # 尾结点即为反转后的链表头结点
        # 开始反转
        current.next.next = current
        return current


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    head = linked_list_util.init_lined_list(nums)
    linked_list_util.print_linked_list(head)
    print('--------')
    s = Solution()
    # s.reverseList1(head, None)
    # print_linked_list(s.head)
    # print('-------')
    linked_list_util.print_linked_list(s.reverseList(head))