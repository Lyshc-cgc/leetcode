# util function


def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

