# 707. 设计链表
# https://programmercarl.com/0707.%E8%AE%BE%E8%AE%A1%E9%93%BE%E8%A1%A8.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
# https://leetcode.cn/problems/design-linked-list/description/

from utils.linked_list_util import print_linked_list

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node()  # 虚拟头结点
        self.tail = self.head  # 尾结点指向，刚开始指向头

    def get(self, index: int) -> int:
        """

        :param index: 从0开始
        :return:
        """
        res_node = self.head
        while res_node and index >= 0:  # index可以为0，表示第一个节点
            res_node = res_node.next
            index -= 1
        if not res_node:  # 下标无效, res_node为空
            return -1
        return res_node.data

    def addAtHead(self, val: int) -> None:
        p = Node(data=val, next=self.head.next)
        self.head.next = p
        if not p.next:  # 若该节点是尾节点
            self.tail = p

    def addAtTail(self, val: int) -> None:
        p = Node(data=val)
        self.tail.next = p
        self.tail = p

    def addAtIndex(self, index: int, val: int) -> None:
        index -= 1  # 先减1，为了找到插入节点的前一个节点
        pre_node = self.head  # 指向待插入节点前一个节点
        while pre_node and index >= 0:
            pre_node = pre_node.next
            index -= 1
        if not pre_node:  # 下标超出链表长度
            return
        p = Node(data=val, next=pre_node.next)  # 插入
        pre_node.next = p
        if not p.next:  # 插入的是尾结点
            self.tail = p

    def deleteAtIndex(self, index: int) -> None:
        index -= 1  # 先减1，为了找到删除节点的前一个节点
        pre_node = self.head  # 指向待删除节点前一个节点
        while pre_node and index >= 0:
            pre_node = pre_node.next
            index -= 1
        if not pre_node or not pre_node.next:  # 下标超出链表长度
            return

        if pre_node.next == self.tail:  #若待删除节点是尾节点
            pre_node.next = pre_node.next.next
            self.tail = pre_node
        else:
            pre_node.next = pre_node.next.next

if __name__ == '__main__':
    obj = MyLinkedList()
    # obj.addAtHead(1)
    # obj.addAtTail(2)
    # obj.addAtIndex(2,3)
    # print(obj.get(0))
    # print(obj.get(1))
    # print(obj.get(2))
    # obj.deleteAtIndex(1)
    # print(obj.get(0))
    # print(obj.get(1))
    # print(obj.get(2))
    obj.addAtHead(7)
    obj.addAtHead(2)
    obj.addAtHead(1)
    obj.addAtIndex(3,0)
    obj.deleteAtIndex(2)
    obj.addAtHead(6)
    obj.addAtTail(4)
    print(obj.get(4))