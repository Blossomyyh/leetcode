
"""
dum->1->2->3->4->5->N
3

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    dummy = ListNode()
    dummy.next = head
    fast, slow = dummy, dummy
    while n:
        fast = fast.next
        n -= 1
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next