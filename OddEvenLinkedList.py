# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or head.next == None: return head
        odd, even, second = head, head.next, head.next
        while odd and odd.next and even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = second
        return head


node = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

Solution().oddEvenList(node)
