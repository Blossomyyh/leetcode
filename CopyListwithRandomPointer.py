# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


"""
A linked list is given such that each node contains an additional random pointer
 which could point to any node in the list or null.
"""


class Solution:
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        if head in self.visitedHash:
            return self.visitedHash[head]

        node = Node(head.val, None, None)
        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this would help us avoid them.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random
        # pointer. Thus we have two independent recursive calls. Finally we update the next and random pointers for
        # the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node


        # Time Complexity:
        # O(N) where N is the number of nodes in the linked list.
        # Space Complexity:
        # O(N). If we look closely, we have the recursion stack and
        # we also have the space complexity to keep track of nodes already cloned
        # i.e. using the visited dictionary.
        # But asymptotically渐进的 asymptote渐近线, the complexity is O(N)O(N).








    """
    best tricky way
    duplicate lists:
    1-2-3-4
    1-1-2-2-3-3-4-4
    p.next.random = p.random.next
    Time Complexity : O(N)O(N)
Space Complexity : O(1)O(1)
    """
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        p = head
#         add duplicate nodes
        while p:
            newNode = Node(p.val, None, None)
            newNode.next = p.next
            p.next = newNode
            p = newNode.next
#         random links --> check p.random whether NOne
        p = head
        while p:
            p.next.random = p.random.next if p.random else None
            p = p.next.next
        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        pold, pnew = head, head.next
        headnew = head.next
        while pold and pnew:
            pold.next = pold.next.next
            pnew.next = pnew.next.next if pnew.next else None
            pold = pold.next
            pnew = pnew.next
        return headnew


class Solution2:
    """
    Iteration and Dict
    O(N) & O(N)
    """
    def __init__(self):
        self.visited = {}

    def getclonedNode(self, node: 'Node'):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head

        old_node = head
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        while old_node:
            new_node.next = self.getclonedNode(old_node.next)
            new_node.random = self.getclonedNode(old_node.random)
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]

    # using dictionary
    def copyRandomList(self, head):
        if not head:
            return
        cur, dic = head, {}
        # copy nodes
        while cur:
            dic[cur] = Node(cur.label)
            cur = cur.next
        cur = head
        # copy random pointers
        while cur:
            if cur.random:
                dic[cur].random = dic[cur.random]
            if cur.next:
                dic[cur].next = dic[cur.next]
            cur = cur.next
        return dic[head]