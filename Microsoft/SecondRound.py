"""

A
B
C  3 2 1

"""

class Hanoi:
    def __init__(self):
        self.step = 0

    def hanoi(self,  N: int, A, B, C):

        # base case
        if N == 1:
            print(A + " --> "+ C + ": " + str(N))
            self.step += 1
            return
        else:
            # n-1 from A --> B
            self.hanoi(N-1, A, C, B)
            # n from A -->C
            print(A + " --> " + C + ": " + str(N))
            self.step += 1
            # n -1 from B --> C
            self.hanoi(N-1, B, A, C)


# hanoi = Hanoi()
# hanoi.hanoi(3, "A", "B", "C")
# print(hanoi.step)

"""
2 pointer -> go through list 
use carry to remmeber 
"""
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next  = next

class Solution:
    def printList(self, node):
        string = ""
        while node:
            string += str(node.val) + "->"
            node = node.next
        print(string + "N")

    def addList(self, listA, listB):
        self.printList(listA)
        self.printList(listB)

        p1 = listA
        p2 = listB
        dummy = Node()
        node = dummy
        carry = 0


        while p1 or p2:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            value = val1 + val2 + carry
            carry, remain = divmod(value, 10)
            print(val1, val2, value, carry, remain)
            newNode = Node(remain)
            node.next = newNode

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            node = node.next

        if carry !=0:
            node.next = Node(carry)


        print("Result: ")
        self.printList(dummy.next)
        return dummy.next

# 2->4 5->6->4
# listA = Node(2, Node(4, Node(3)))
# listB = Node(5, Node(6, Node(4)))
# listA = Node(2, Node(4))
# listB = Node(5, Node(6, Node(4)))
listA = Node(0)
listB = Node(0)
listA = Node(2, Node(4))
listB = Node(5, Node(6))
Solution().addList(listA, listB)






