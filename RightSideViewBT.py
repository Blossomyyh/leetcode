# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        res = []
        # bfs
        if not root:
            return res
        queue = deque()
        queue.append(root)
        while queue:
            res.append(queue[-1].val)
            newq = deque()
            for a in queue:
                if a.left:
                    newq.append(a.left)
                if a.right:
                    newq.append(a.right)
            queue = newq

        return res

    def dfs(self, root: TreeNode):
        res = []

        """
        use dfs search 
            remember the level
            go right first
            go left if no right
            check len(res) == curlevel:
                append this node
        """
        def dfs(node, level):
            # base case
            if len(res)==level-1:
                res.append(node.val)
            if node.right:
                dfs(node.right, level+1)
            if node.left:
                dfs(node.left, level +1)

        dfs(root, 1)
        return res