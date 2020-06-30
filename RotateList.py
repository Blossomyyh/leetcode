# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"({self.val},{self.next})"

    #  try printing, simply improved the result of it
    # one of Python’s “dunder” (double-underscore) methods and gets called when you try to convert an object into a string
    # through the various means that are available
    # >> > str(my_car)
    # 'a red car'
    # >> > '{}'.format(my_car)
    # 'a red car'
    #
    # The fact that these methods start and end in double underscores is simply a naming convention
    # to flag them as core Python features.
    # https://dbader.org/blog/python-repr-vs-str

    # f'Car({self.color!r}, {self.mileage!r})'
    #  __class__.__name__ attribute, which will always reflect the class’ name as a string.
    # The string returned by __str__() is the informal string representation of an object and should be readable.
    # The string returned by __repr__() is the official representation and should be unambiguous. !r
    # >> > f"{new_comedian}"
    # 'Eric Idle is 74.'
    # >> > f"{new_comedian!r}"
    # 'Eric Idle is 74. Surprise!'
    # https://realpython.com/python-f-strings/#python-f-strings-the-pesky-details

    def __str__(self):
        return f'a {self.val} node'


"""fast low mod solution"""


# time : O(n) space : O(1)

class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        if not head or not head.next or k == 0:
            return head
        # close the linked list into a ring
        p = head
        # defaults to none and 0
        list_len = 0
        # do a preprocess path O(n), just to figure out how long the link is
        while p != None:
            p = p.next
            list_len += 1
        k %= list_len

        slow, fast = head, head

        # n-k times, k is the rotation you want to do
        for i in range(k):
            fast = fast.next

        # advance both fast and slow pointer until we get to the end of the list
        # make sure fast stops right before the end
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # then there's going to be some pointer arithmetic O(1)
        fast.next = head
        head = slow.next
        slow.next = None
        return head
