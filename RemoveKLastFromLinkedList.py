class Node(object):
    def __init__(self, val, next = None):
        self.val  = val
        self.next = next
    def __str__(self):
        node = self
        answer = ''
        while node:
            answer += str(node.val)
            node = node.next
        return answer
"""
2 node, one point at the end, one point at previous k 
pre->....k ->node->None
pre equal node.nexg

"""
class Solution(object):
    def removeKLastNode(self, linkedList, k):
        node = linkedList
        previous = linkedList
        while k:
            node = node.next
            k -= 1
        """
        edge case!! 
        \\delete head!!!!!
        if node.next == none
        """
        if not node:
            return node.next


        while node.next:
            node = node.next
            previous = previous.next
        # previous
        previous.next = previous.next.next
        return linkedList
head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
print(head)
print(Solution().removeKLastNode(head, 2))

"""
6->N, 6
let node = 6 and prev = dummy and dummy.next = 6
if 6 == 6
    prev.next = None
    node =None

"""


class Solution:
    def removeElements(self, head: Node, val: int) -> Node:
        dummy = Node(0, head)
        node, prev = head, dummy
        while node:
            if node.val == val:
                prev.next = node.next
                node = prev.next
            else:
                prev = node
                node = node.next
        return dummy.next




