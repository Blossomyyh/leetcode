"""

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSymmetric(self, root: TreeNode) -> bool:
    def compare(t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        return t1.val==t2.val and compare(t1.left, t2.right) and compare(t1.right, t2.left)

    return compare(root, root)

import collections
def iterative(root):
    if not root: return True

    q = collections.deque()
    q.append(root.left)
    q.append(root.right)

    while q:
        left, right = q.popleft(), q.popleft()

        if not left and not right:
            continue
        elif left and right and left.val == right.val:
            pass
        else:
            return False

        q.append(left.left)
        q.append(right.right)
        q.append(left.right)
        q.append(right.left)

    return True