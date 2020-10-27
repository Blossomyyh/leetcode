"""
102. Binary Tree Level Order Traversal

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

out:[[3],[9,20],[15,7]]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def levelOrder(self, root: TreeNode):
    if not root: return []
    res = [[root.val]]
    curlevel = [root]

    while curlevel:
        nextlevel = []
        levelval = []
        for node in curlevel:
            if node.left:
                levelval.append(node.left.val)
                nextlevel.append(node.left)
            if node.right:
                levelval.append(node.right.val)
                nextlevel.append(node.right)
        if levelval:
            res.append(levelval)

        curlevel = nextlevel
    return res

