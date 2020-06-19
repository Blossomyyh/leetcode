class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


def getTwoPIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
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
