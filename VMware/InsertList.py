"""
1 -> 3 -> 5 -> 7 -> 11
Insert 8
1 -> 3 -> 5 -> 7 ->8 => 11
"""
"""
Implement Sorted Linklist with insert method
"""


class ListNode:
    def __init__(self, val=0, nextVal=None):
        super().__init__()
        self.val = val
        self.next = nextVal


class LinkedList:
    def __init__(self, linkedlist):
        super().__init__()
        self.linkedlist = linkedlist

    def insert(self, x):
        # prev and cur pointer
        dummy = ListNode()
        dummy.next = self.linkedlist
        prev, curr = dummy, self.linkedlist
        # traversal the list
        while curr and curr.val < x:
            prev = prev.next
            curr = curr.next
        # insert x
        newNode = ListNode(x)
        # print(newNode, "new")
        prev.next = newNode
        newNode.next = curr
        # change head to dummynext
        self.linkedlist = dummy.next
        return newNode

    def printList(self):
        node = self.linkedlist
        while node:
            print(node.val)
            node = node.next


if __name__ == '__main__':
    lists = ListNode(1, ListNode(3, ListNode(5, ListNode(7, ListNode(11)))))
    linked = LinkedList(lists)
    linked.printList()
    linked.insert(-1)
    linked.insert(15)
    print('-------')
    linked.printList()