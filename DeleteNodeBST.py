"""
450. Delete Node in a BST

Given a root node reference of a BST and a key,
delete the node with the given key in the BST.

delete node in BST:

1. no children
2. only right children
    X predecessor -> up to parent level to find
    Y successor -> right children
    (1) use successor to replace
    (2) delete successor
3. has left children (may have right)
    X successor -> up to parent level to find
    Y predecessor -> left children
    (1) use predecessor to replace
    (2) delete successor


"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    """successor --> bigger - righttree & least node"""
    def successor(self, node):
        # first go right tree
        node = node.right
        # go left to find min
        while node.left:
            node = node.left
        return node.val

    """predecessor --> smaller - lefttree & max node"""
    def predecessor(self, node):
        # go left tree
        node = node.left
        # go right to find max
        while node.right:
            node = node.right
        return node.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None


        """do recursive to find delete node"""

        if root.val == key:
            if not root.right and not root.left:
                root = None
            elif root.right:
                ## only right or all
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                ## only left
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        elif key < root.val:
            ## go left and make sure assign to the new left node
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            ## go right and make sure assign to the new right node
            root.right = self.deleteNode(root.right, key)

        return root