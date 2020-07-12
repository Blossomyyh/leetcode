# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from collections import deque


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        """
        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4 
        """
        slow, fast = head, head
        # when even -> slow point to the second half
        # when odd -> slow point to the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        """
        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        """

        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # prev is the head of reversed linkedlist

        """
        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        """
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next



