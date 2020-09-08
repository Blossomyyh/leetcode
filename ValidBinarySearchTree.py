# valid binary search tree
# should
#
#     5
#     /\
#    4  7
#      /
#      2
#   X
# have restrictions on both upper and lower bound
# traversal the tree and pass down
#
#
# Pseudo code:
# low < n.val < high
# isValid(n.left, low, n.val)
# isValid(n.right, n.val, high)
# if node is null return True
"""recursive -- and 3 conditions together"""
# in terms of
# time complexity: we just go through each node once --> O(n) linear
# space complexity: is going to be proportional to the size of the recursive stack that we building
# like you can just keep recursing down and down and start building up this function stack
# is linear with regards to this input O(N)


class Node(object):
    def __init__(self, val, left = None, right = None ):
        self.val = val
        self.left = left
        self.right = right



class Solution :
    """iteration"""
    def validHelper(self, node, low, high):
        if not node: return True
        val = node.val
        if low < val < high and self.validHelper(node.left, low, val) and self.validHelper(node.right, val, high):
            return True
        return False
    def validBinarySearchTree(self, node: Node):
        if not node: return True
        return self.validHelper(node, float('-inf'), float('inf'))


    """recursive: use stack"""

    def isValidBST(self, root: Node) -> bool:
        #         iteration with stack!! important
        if not root: return True
        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            node, low, high = stack.pop()
            if not node: continue
            if low < node.val < high:
                stack.append((node.left, low, node.val))
                stack.append((node.right, node.val, high))
            else:
                return False
        return True



    """inorder """


    def isValidBST(self, root: Node) -> bool:
        stack, inorder_lower = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.

            if root.val <= inorder_lower:
                return False
            inorder_lower = root.val
            root = root.right
        return True

#   5
#  / \
# 4   7
node = Node(5)
node.left = Node(4)
node.right = Node(7)
print(Solution().isValidBST(node))

#   5
#  / \
# 4   7
#    /
#   2
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.left = Node(2)
print(Solution().validBinarySearchTree(node))
# False