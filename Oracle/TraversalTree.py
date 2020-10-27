"""
144. Binary Tree Preorder Traversal

1. recursive
2. non recursive
O(n) O(n)
"""

class TreeNode:
    def __init__(self, val, r, l):
        self.val = val
        self.right = r
        self.left = l
def preorderTraversal(self, root: TreeNode) :
    # root, left, right
    if not root: return []
    res = []

    def dfs(node):
        res.append(node.val)
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)

    dfs(root)

    """ iterative -- root pop, \\right!! append, \\left append """
    out = []
    stack = [root]
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res

"""
94. Binary Tree Inorder Traversal
Morris Traversal

"""

def inorderTraversal(self, root: TreeNode):
    #  left,root, right
    if not root: return []
    res = []

    def dfs(node):

        if node.left:
            dfs(node.left)
        res.append(node.val)
        if node.right:
            dfs(node.right)

    dfs(root)

    # nonrecursive

    stack = []
    out = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        out.append(node.val)
        node = node.right

    return res


"""
145. Binary Tree Postorder Traversal
while stack
    pop root append val
    append \\left
    append \\right
\\ reverse for list
"""


def postorderTraversal(self, root: TreeNode):
    # left, right , root
    if not root: return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    """use reverse to get post order!"""
    return res[::-1]

