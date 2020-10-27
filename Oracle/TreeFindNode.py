"""
236. Lowest Common Ancestor of a Binary Tree

 ''' top root; pis ancestor, q'''

    use 3 boolean to record
    when 2 of them is true -> current node is LCA

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    if not root: return None

    ''' top root; pis ancestor, q'''
    """
    use 3 boolean to record
    when 2 of them is true -> current node is LCA
    """
    ans = root
    def recurse_tree(current_node):

        # If reached the end of a branch, return False.
        if not current_node:
            return False

        # Left Recursion
        left = recurse_tree(current_node.left)

        # Right Recursion
        right = recurse_tree(current_node.right)

        # If the current node is one of p or q
        mid = current_node == p or current_node == q

        # If any two of the three flags left, right or mid become True.
        if mid + left + right >= 2:
            ans = current_node

        # Return True if either of the three bool values is True.
        return mid or left or right

    # Traverse the tree
    recurse_tree(root)
    return ans


def LCAiterative(root, p, q):
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
        node = stack.pop()
        # While traversing the tree, keep saving the parent pointers.
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    ancestor = set()
    while p:
        ancestor.add(p)
        p = parent[p]

    while q not in ancestor:
        q = parent[q]
    return q


def findBottomLeftValue(root: TreeNode) -> int:
    if not root: return None
    global maxDepth
    maxDepth = 0

    def helper(node, level, maximum):
        if not node:
            return
        if level > maximum:
            maxDepth =max(maximum, level)
            leftres = node
        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right.left, level + 2)

    leftres = root
    helper(root, 0, 0)

    return leftres.val

print(findBottomLeftValue(TreeNode(1, None, None)))

"""
617. Merge Two Binary Trees
Given two binary trees and imagine that when you put one of them to cover the other, 
some nodes of the two trees are overlapped while the others are not.

"""
def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1:
        return t2
    if not t2:
        return t1
    t1.val += t2.val

    t1.left = self.mergeTrees(t1.left, t2.left)
    t1.right = self.mergeTrees(t1.right, t2.right)
    return t1



"""
671. Second Minimum Node In a Binary Tree
"""


def findSecondMinimumValue(self, root: TreeNode) -> int:
    # root.val = min(root.left.val, root.right.val) always holds.
    self.ans = float('inf')
    min1 = root.val

    def dfs(node):
        if node:
            if min1 < node.val < self.ans:
                self.ans = node.val
            elif node.val == min1:
                dfs(node.left)
                dfs(node.right)

    dfs(root)
    return self.ans if self.ans < float('inf') else -1