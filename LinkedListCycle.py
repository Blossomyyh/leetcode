class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""detect cycle in linked list"""


class Solution1:
    # 1.Using extra storage time = O(N), space = O(N)
    # 2.Two Pointers, time = O(N) space = O(1)

    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        # p1 advance 1 step at a time, while p2 - 2
        while slow != fast:
            if not fast or not fast.next: return False
            slow, fast = slow.next, fast.next.next
        return slow is not None


"""detect beginning of the cycle in linked list"""


class Solution2:
    #  sol1:   hashtable tack
    #  sol2:   Floyd's Tortoise and Hare

    def intersection(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
                #  the importance of creating a new func -> wipe out exceptions like only one node with no cycle
        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        """phase 1"""

        inter = self.intersection(head)
        if inter is None:
            return None
        p = head
        while p != inter:
            p = p.next
            inter = inter.next
        return p
        #  time complexity   O(n)

        # fast runner (a hare) races a slow runner (a tortoise) on a circular track
        #  Floyd's algorithm is separated into two distinct phases
        #  In the first phase, it determines whether a cycle is present in the list.
        #   If no cycle is present, it returns null immediately,
        #  it is impossible to find the entrance to a nonexistant cycle.
        #  Otherwise, it uses the located "intersection node" to find the entrance to the cycle.

        # formula : 2(F+a) = F+ a+b+a -> F = b


node1 = ListNode(3, None)
node2 = ListNode(2, None)
node3 = ListNode(0, None)
node4 = ListNode(4, None)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(Solution2().detectCycle(node1))