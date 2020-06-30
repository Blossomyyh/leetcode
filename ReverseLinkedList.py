# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        res = str(self.val)
        if self.next:
            res += str(self.next)
        return res

# time O(N+K), which is O(n).
# space O(1)
class Solution:
    """iteration"""
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            # python tackle statement from right side
            # curr.next, prev, curr = prev, curr, curr.next
        return prev

    """recursive"""

    def reverseList(self, head):
        return self.reverse(head, None)

    def reverse(self, curr: ListNode, prev: ListNode):
        if not curr:
            return prev
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        return self.reverse(curr, prev)

node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(Solution().reverseList(node))

