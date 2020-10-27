import unittest


class ListNode:
    def __init__(self, val=0, nextPoint=None):
        self.val = val
        self.next = nextPoint


class Solution:
    # 1->2->3->N
    # 3->2->1->N
    def reverseList(self, listNode):
        # prev cur

        prev, curr = None, listNode
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # print the list =
        self.printList(prev)
        return prev

    def printList(self, head):
        res = []
        while head != None:
            res.append(head.val)
            head = head.next
        print(res)


class test(unittest.TestCase):
    def testReverse(self):
        linkedlist = ListNode(1, ListNode(2, ListNode(3)))
        Solution().reverseList(linkedlist)
        # self.assertEqual()


if __name__ == '__main__':
    unittest.main()