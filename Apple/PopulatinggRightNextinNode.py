"""
116. Populating Next Right Pointers in Each Node

"""
class Node:
    def __init__(self, val: int = 0, left = None, right= None, next= None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque
class Solution:
    def connect(self, root):
        # level order traversal
        if not root:
            return root
        queue =deque()
        queue.append(root)
        while queue:
            newqueue = []
            prev = None
            while queue:
                cur = queue.pop()
                cur.next = prev
                # add next level
                if cur.right:
                    newqueue.append(cur.right)
                if cur.left:
                    newqueue.append(cur.left)
                prev = cur
            """ add right + left ==> reverse newqueue"""
            queue = newqueue[::-1]
            print(queue)
        return root


"""
sol 2
useing next pointer

 leftmost = root
 while (leftmost.left != null)
 {
     head = leftmost
     while (head.next != null)
     {
         1) Establish Connection 1
         2) Establish Connection 2 using next pointers
         head = head.next
     }
     leftmost = leftmost.left
 }
"""