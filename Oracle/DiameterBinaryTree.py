"""

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    """

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        #  calculate how many nodes.
        self.ans = 1

        def recursive(node):
            if not node:
                return 0
            L = recursive(node.left)
            R = recursive(node.right)
            # update ans, 1, is root
            self.ans = max(self.ans, L+R+1)
            return max(L, R)+1
        recursive(root)
        # length is represented by number of edges between them
        return self.ans-1
