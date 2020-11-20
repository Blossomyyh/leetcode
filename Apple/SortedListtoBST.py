class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head):
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)

    # find mid - not None
    slow = head
    fast = head.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # tmp points to root
    tmp = slow.next

    # cut down the left child
    slow.next = None

    root = TreeNode(tmp.val)
    root.left = sortedListToBST(head)
    root.right = sortedListToBST(tmp.next)

    return root

