class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""sample code from techpro"""

class Solution(object):
    def _length(self, n):
        len = 0
        curr = n
        while curr:
            curr = curr.next
            len += 1
        return len

    def intersection(self, a: ListNode, b: ListNode):
        lenA = self._length(a)
        lenB = self._length(b)
        currA, currB = a, b

        if lenA > lenB:
            # then we advance curr A
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next

        # Now a and b are pretty much at the same distance to the end of list
        # we advance both of them in sync until we figure out where are they meet
        while currA != currB:
            currA, currB = currA.next, currB.next
        # return either current A or B
        return currA



"""solution 1: use set to store nodes in A -- time limits exceed"""


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    # hashset: traversal A and store node val in set and check whether node in B exists in the set as well

    # two pointer
    setA = []
    # step 1: travelsal headA, and store each node in a dict
    while headA:
        setA.append(headA)
        headA = headA.next
    # step 2: travel headB, check each node if in dict
    while headB:
        # if checked, return the headB node = intersctionNode
        if headB in setA:
            return headB
        headB = headB.next
    return None


""" 
# Time complexity : O(m+n)

# Space complexity : O(1).
"""


# Run both out to the end/tail
#         If the tails aren't identical they didn't intersect, RETURN NULL
#         You know:
#         - They intersect
#         - ListA's length
#         - ListB's length
#         lenA == lenB exactly the same, walk fwd from heads to find intersect
#         lenA  > lenB skip ListA (lenA-lenB) nodes ahead, walk fwd to find intersect
#         lanB  > lenA skip ListB (lenB-lenA) nodes ahead, walk fwd to find intersect

def getTwoPIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    # two pointer
    if headA == None or headB == None:
        return None
    a, b = headA, headB
    la, lb = 0, 0
    while headA:
        la += 1
        headA = headA.next
    while headB:
        lb += 1
        headB = headB.next

    if la > lb:
        # listA is longer, skip it ahead
        dif = la - lb
        while dif != 0:
            a = a.next
            dif -= 1
    elif la < lb:
        dif = lb - la
        while dif != 0:
            b = b.next
            dif -= 1
    while a and b:
        if a == b:
            return a
        a = a.next
        b = b.next

    return None


"""
most tricky one:
let a, b go through both listA and listB
the total length of which they go through is the same : lenA+ lenB
if there is an intersection for A and B, then pA and pB will meet at the intersection for sure
"""


def simpleSolution(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    a, b = headA, headB

    while a != b:
        a = headB if not a else a.next
        b = headA if not b else b.next
    return a