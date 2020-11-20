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
            print(self.ans)
            return max(L, R)+1
        recursive(root)
        # length is represented by number of edges between them
        return self.ans-1

n = TreeNode(0, TreeNode(1, TreeNode(3, TreeNode(2)), TreeNode(4, TreeNode(5))))
Solution().diameterOfBinaryTree(n)

"""
1245. Tree Diameter
Each node has labels in the set {0, 1, ..., edges.length}.
Input: edges = [[0,1],[0,2]]
Output: 2
A longest path of the tree is the path 1 - 0 - 2.

"""



from collections import defaultdict
def diameterinGraph(self, edges: [[int]]):
    graph = defaultdict(set)
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    # build tree by graph
    # BFS traversal
    self.dia = 0
    seen = set()

    def dfs(node):
        l1 = l2 = 0
        seen.add(node)
        # get all depth from its children/p
        for nei in graph[node]:
            if nei not in seen:
                # get d ->depth + itself
                d = dfs(nei)
                # maintain max 2 value in l1l2
                if d > l1:
                    l1, l2 = d, l1
                elif d > l2:
                    l2 = d
        # update diameter by
        self.dia = max(self.dia, l1 + l2)
        # return top depth +1(itself)
        return l1 + 1

    dfs(0)
    return self.dia

