# util function

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def init_lined_list(nums):
    index = head = ListNode(nums[0])
    for e in nums[1:]:
        index.next = ListNode(e)
        index = index.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

