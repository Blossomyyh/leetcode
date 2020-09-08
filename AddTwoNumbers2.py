class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """using list->int->list"""

    # The basic idea is to convert the linked lists to integer values (using a similiar approach as atoi).
    # Then create a new linked list from the sum by adding the digits in reverse.

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self.getInt(l1) if l1 else 0
        n2 = self.getInt(l2) if l2 else 0
        return self.getList(n1 + n2) if (n1+n2) !=0 else ListNode(0)

    def getInt(self, l : ListNode):
        ret = 0
        while l:
            ret = ret*10 + l.val
            l = l.next
        return ret

    def getList(self, n):
        cur = None
        while n >0:
            n, left = divmod(n, 10)
            cur = ListNode(left, cur)
        return cur



    """using stack"""
    def addTwoNumber(self, l1, l2):
        s1 = []
        s2 = []

        curr1, curr2 = l1, l2

        while (curr1 or curr2):
            if curr1: s1.append(curr1.val)
            if curr2: s2.append(curr2.val)

            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next

        head = None
        acc = 0
        while (len(s1) > 0 or len(s2) > 0):
            val1 = s1.pop() if len(s1) > 0 else 0
            val2 = s2.pop() if len(s2) > 0 else 0
            val = val1 + val2 + acc

            head = ListNode(val % 10, head)

            acc = val // 10

        if acc > 0: head = ListNode(acc, head)

        return head

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
# 342 + 465 = 807
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


answer = Solution().addTwoNumbers(l1, l2)
while answer:
    print(answer.val, end=' ')
    answer = answer.next
    # 807