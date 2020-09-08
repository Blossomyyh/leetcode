"""
enumerate()

min((val, i)for i, val in... if xxx)

"""
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
from typing import List

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    # will implement a string function, just quickly print out the linklist
    # help us evaluate whether the function is ok or not
    def __str__(self):
        c = self
        answer = ''
        while c:
          answer += str(c.val) if c.val else ""
          c = c.next
        return answer

    # simplest way, append all and sorted
    def merge(self, node):
        # fill it later on
        arr = []
        for n in node:
            while n:
                arr.append(n.val)
                n = n.next
        head = root = None
        for val in sorted(arr):
            # if root is None
            if not root:
                head = root = ListNode(val)
            else:
                root.next = ListNode(val)
                root = root.next

        return head

    #     NlogN time sorted
    """
    linear time
    go and compare 
    """


def merge2(lists):
    # dummy head !!
    head = curr = ListNode(-1)
    # any of the head is not None
    while any(list is not None for list in lists):
        curr_min, i = min((list.val, i) for i, list in enumerate(lists) if list is not None)
        lists[i] = lists[i].next
        curr.next = ListNode(curr_min)
        curr = curr.next
    return head.next
#     O(NlogN)

"""
Time complexity : O(N\log N) where N is the total number of nodes.
Collecting all the values costs O(N) time.
A stable sorting algorithm costs O(N\log N) time.
Iterating for creating the linked list costs O(N)time.

Space complexity : O(N).

Sorting cost O(N)O(N) space (depends on the algorithm you choose).
Creating a new linked list costs O(N)O(N) space.
"""


# and let me create a driver function
a = ListNode(1, ListNode(3, ListNode(5)))
b = ListNode(2, ListNode(4, ListNode(6)))
print(a)
print(b)
print(merge2([a, b]))


"""
best solution:
Priority queue
"""

import heapq
class Solution3(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
# python heapq as priority queue.
        head = curr = ListNode(None)
#     h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        """!!!if l --> l is not NONE!!!"""
        h = [(l.val, ix) for ix, l in enumerate(lists) if l]
        """heapq.heapify(h)"""
        heapq.heapify(h)
        while h:
            val,ix = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            lists[ix] = lists[ix].next
            """compare if lists[ix] is not NONE!!!!!!"""
            if lists[ix]:
                heapq.heappush(h, (lists[ix].val, ix))
        return head.next


"""
Time complexity : O(N\log k)O(Nlogk) where \text{k}k is the number of linked lists.

The comparison cost will be reduced to O(\log k)O(logk) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1)O(1) time.
There are NN nodes in the final linked list.
Space complexity :

O(n)O(n) Creating a new linked list costs O(n)O(n) space.
O(k)O(k) The code above present applies in-place method which cost O(1)O(1) space. And the priority queue (often implemented with heaps) costs O(k)O(k) space (it's far less than NN in most situations).
"""




# Approach 5: Merge with Divide And Conquer
"""

This approach walks alongside the one above but is improved a lot. We don't need to traverse most nodes many times repeatedly

Pair up \text{k}k lists and merge each pair.

After the first pairing, \text{k}k lists are merged into k/2k/2 lists with average 2N/k2N/k length, then k/4k/4, k/8k/8 and so on.

Repeat this procedure until we get the final sorted linked list.

Thus, we'll traverse almost NN nodes per pairing and merging, and repeat this procedure about \log_{2}{k}log 
2
 k times.
"""

class Solution4(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
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
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists



# After the first pairing, \text{k}k lists are merged into k/2k/2 lists with average 2N/k2N/k length,
# then k/4k/4, k/8k/8 and so on.



"""
Time complexity : O(N\log k)O(Nlogk) where \text{k}k is the number of linked lists.

We can merge two sorted linked list in O(n)O(n) time where nn is the total number of nodes in two lists.
Sum up the merge process and we can get: O\big(\sum_{i=1}^{log_{2}{k}}N \big)= O(N\log k)O(∑ 
i=1
log 
2
​	
 k
​	
 N)=O(Nlogk)
Space complexity : O(1)O(1)

We can merge two sorted linked lists in O(1)O(1) space.
"""