# 24. 两两交换链表中的节点
# https://programmercarl.com/0024.%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/swap-nodes-in-pairs/description/

from typing import Optional
from utils import linked_list_util

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归版本
        :param head:
        :return:
        """
        if not head:  # 空
            return None
        if not head.next:  # 只有1个结点
            return head
        left = head  # 指向两组中的第一个
        right = head.next  # 第二个
        if not right:   # 该组中第二个结点为空，不用交换，返回
            return
        else:
            tmp_right_next = self.swapPairs(right.next)  # 向右前往下一组进行交换, 用目前组右边节点的指针指向返回值
        # 交换
        right.next = left
        left.next = tmp_right_next

        return right  # 新的左节点

    def swapPairs1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        循环版本
        :param head:
        :return:
        """
        pass

if __name__ == '__main__':
    nums = [1,2,3,4]
    head = linked_list_util.init_lined_list(nums)
    linked_list_util.print_linked_list(head)
    print('--------')
    linked_list_util.print_linked_list(Solution().swapPairs(head))