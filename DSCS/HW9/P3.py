from linked_list_helper import ListNode


def P3(head: ListNode) -> ListNode:
    ##### Write your Code Here #####
    fst = ListNode(None)
    node = head
    while node:
        nxt = node.next
        node.next = fst.next
        fst.next = node
        node = nxt
    return fst.next
    ##### End of your code #####
