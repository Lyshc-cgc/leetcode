# 203. 移除链表元素
# https://programmercarl.com/0203.%E7%A7%BB%E9%99%A4%E9%93%BE%E8%A1%A8%E5%85%83%E7%B4%A0.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/remove-linked-list-elements/description/
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        linked_list = ListNode(0, head)  # 构造一个新的头节点，指向原来的头节点,作为链表引用
        index = linked_list  # 指针
        while index.next:  # 下一个节点不为空
            if index.next.val == val:  # 下一个节点是需要删除的节点
                index.next = index.next.next  # 删除该节点
            else:
                index = index.next  # 移动指针
        return linked_list.next

if __name__ == '__main__':
    nums = [1, 2, 6, 3, 4, 5, 6]
    index = head = ListNode(1)
    for e in nums[1:]:
        index.next = ListNode(e)
        index = index.next
    res_linked_list = Solution().removeElements(head, 6)
    while(res_linked_list):
        print(res_linked_list.val)
        res_linked_list = res_linked_list.next