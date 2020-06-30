class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = pre = ListNode(None)
        curr.next = head   # also need to check head.val thus cannot let curr = head
        dummy = pre   # which node to point to yet to be determined
        while curr and curr.next:
            if curr.val == curr.next.val:
                val = curr.val   # stor the repeated value for further checking
                while curr and curr.val == val:   # check further (the third, the fourth, ...)
                    curr = curr.next
                pre.next = curr   # pre -> the first curr with curr.val != val
            else:   # increment both pre and curr
                pre = curr
                curr = curr.next
        return dummy.next