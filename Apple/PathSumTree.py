"""
112. Path Sum
O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if not root: return False

    # make sure node is a leaf

    if root.val == sum and not root.left and not root.right:
        return True
    else:
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


"""recursive"""


def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if not root:
        return False
    stack = [(root, sum - root.val)]
    while stack:
        node, cur = stack.pop()
        if cur == 0 and not node.left and not node.right:
            return True
        if node.right:
            stack.append((node.right, cur - node.right.val))
        if node.left:
            stack.append((node.left, cur - node.left.val))
    return False

"""
113. Path Sum II

For every leaf, we perform a potential O(N)operation of copying over the pathNodes nodes 
to a new list to be added to the final pathsList. 
Hence, the complexity in the worst case could be
O(n2)

space O(n)
"""


class Solution:
    def recursive(self, node, cur, path):
        if not node:
            return
        """ check whether is leaf node"""
        if cur == 0 and not node.left and not node.right:
            self.res.append(path)
            return
        """ no need to add cur<sum...  -- may have negative nums"""
        """ only need to append Val in list!! """
        if node.left:
            self.recursive(node.left, cur - node.left.val, path + [node.left.val])
        if node.right:
            self.recursive(node.right, cur - node.right.val, path + [node.right.val])

    def pathSum(self, root: TreeNode, sum: int):
        if not root: return []

        # make sure node is a leaf

        self.res = []

        self.recursive(root, sum - root.val, [root.val])
        return self.res


"""  
437. Path Sum III

use preorder to traversal tree 
use dictionary to record sum and counts
\\ Prefix Sum
    === Number of Continuous Subarrays that Sum to Target
\\ preorder traversal
    need dic[cur] -= 1 to prevent parallel


"""
from collections import defaultdict


class Solution:
    def pathSum(self, root, target):
        dic = {0: 1}
        self.count = 0

        def dfs(node, sums):
            if not node:
                return
            cur = sums + node.val
            if cur - target in dic:
                self.count += dic[cur - target]

            dic[cur] = dic.get(cur, 0) + 1

            dfs(node.left, cur)
            dfs(node.right, cur)

            # remove the current sum from the hashmap
            # in order not to use it during
            # the parallel subtree processing
            dic[cur] -= 1

        dfs(root, 0)
        return self.count

















