import heapq
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
Merge with Divide And Conquer
Time complexity : O(N\log k)O(Nlogk) where \text{k}k is the number of linked lists.

Pair up \text{k}k lists and merge each pair.

After the first pairing, \text{k}k lists are merged into k/2k/2 lists with average 2N/k2N/k length, then k/4k/4, k/8k/8 and so on.

Repeat this procedure until we get the final sorted linked list.



"""

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #         Pair up \text{k}k lists and merge each pair.
        if lists is None or len(lists) == 0: return None
        amount = len(lists)

        interval = 1

        def merge2list(l1, l2):
            head = curr = ListNode(None)
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2

            return head.next

        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = merge2list(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]