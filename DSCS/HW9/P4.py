from linked_list_helper import ListNode


def P4(num1: ListNode, num2: ListNode) -> ListNode:
    ##### Write your Code Here #####
    def inverse(head: ListNode) -> ListNode:
        fst = ListNode(None)
        node = head
        while node:
            nxt = node.next
            node.next = fst.next
            fst.next = node
            node = nxt
        return fst.next
    num1 = inverse(num1)
    num2 = inverse(num2)
    carry = 0
    fst = ListNode(None)
    while num1 or num2:
        val = carry + (num1.val if num1 else 0) + (num2.val if num2 else 0)
        carry = val//10
        val %= 10
        node = ListNode(val)
        node.next = fst.next
        fst.next = node
        num1 = num1.next if num1 else None
        num2 = num2.next if num2 else None
    if carry:
        node = ListNode(carry)
        node.next = fst.next
        fst.next = node
    return fst.next
    ##### End of your code #####
