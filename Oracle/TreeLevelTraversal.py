"""
102. Binary Tree Level Order Traversal

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode):
        if not root: return []
        queue = [root]
        res = []
        while queue:
            curres = []
            nextlevel = []
            for node in queue:
                curres.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            res.append(curres)
            queue = nextlevel


        # recursive -- bottom up
        l = []
        def helper(node, level):
            if len(l) == level:
                # init level
                l[level] = []

            l[level].append(node.val)
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
        helper(root, 0)
        print(l[::-1])
        return res

    """
    bottom up 
    
    res[::-1] at last
    """

    def zigzagLevelOrder(self, root: TreeNode):
        # left-right & right to left for each 2 level
        if not root: return []
        queue = [root]
        res = []
        level = 0
        while queue:
            curres = []
            nextlevel = []
            level += 1
            for node in queue:
                curres.append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            if level % 2 == 0:
                res.append(curres[::-1])
            else:
                res.append(curres)
            queue = nextlevel
        return res

    """
    traversal vertical
    1. use dic
    2. go dfs record col and level
    3. sort item by level
    """
    def verticalOrder(self, root: TreeNode):
        if not root: return []
        res = []
        dic = {}

        def helper(node, col, level):
            if col not in dic:
                dic[col] = []
            dic[col].append([level, node.val])
            if node.left:
                helper(node.left, col - 1, level + 1)
            if node.right:
                helper(node.right, col + 1, level + 1)

        helper(root, 0, 0)
        cols = list(dic.keys())
        for c in sorted(cols):
            dic[c].sort(key=lambda x: x[0])
            cur = []
            for i in dic[c]:
                cur.append(i[1])
            res.append(cur)
        return res


