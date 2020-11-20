"""
InvertBinaryTree

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
recursive
"""
def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return root
    """have to use swap here!!!!"""
    root.right, root.left = invertTree(root.left), invertTree(root.right)
    return root

"""
iterative
"""
from collections import deque
def invertTree( root: TreeNode) -> TreeNode:
    if not root:
        return root
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        node.right, node.left = node.left, node.right
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return root