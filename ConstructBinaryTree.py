"""
105. Construct Binary Tree from Preorder and Inorder Traversal

recursive find root from preorder
get idx of root in inorder
find left sub and right sub (preorder & inorder) based on length
"""
"""
\\ improvement:
  hashmap to store value <-> index in postorder


left : startpre+1
        startin
        idx-1
right : startpre+1+(idx-startin)
        idx+1
        endin

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        # dfs for left and right children for a node

        def helper(startpre, startin, endin):
            # bottom case
            if startin>endin:
                return None

            # find root
            root = TreeNode(preorder[startpre])
            # find idx for root
            idx = -1
            for i in range(startin, endin+1):
                if inorder[i]==preorder[startpre]:
                    idx = i
                    break
            print(idx, preorder[startpre])
            if idx != -1:
                # find left subtree
                print(startpre+1, startin, idx-1)
                root.left = helper(startpre+1, startin, idx-1)
                # find right subtree
                # right start will be lengthleft+ start
                print(startpre+1+(idx-startin), idx+1, endin)
                root.right = helper(startpre+1+(idx-startin), idx+1, endin)

            return root
        return helper(0, 0, len(inorder)-1)

preorder = [1, 2, 3]
inorder = [2, 3, 1]
Solution().buildTree(preorder, inorder)

"""
106. Construct Binary Tree from Inorder and Postorder Traversal

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

 right: endpost - 1
        idx + 1
        endin
 
 left:  endpost - 1 - (endin - idx)
        startin
        idx - 1
"""


class Solution:
    def helper(self, endpost, startin, endin, inorder, postorder):
        # base
        if startin > endin:
            return None
        # build root
        root = TreeNode(postorder[endpost])

        # find root in inorder
        """ use hashmap to get index"""
        idx = inorder[root.val]
        if idx != -1:

            """post do right first --> right root first"""
            root.right = self.helper(endpost - 1, idx + 1, endin, inorder, postorder)

            # right root --> root-1-(length of left tree)

            root.left = self.helper(endpost - 1 - (endin - idx), startin, idx - 1, inorder, postorder)
        return root

    def buildTree(self, inorder: [int], postorder: [int]) -> TreeNode:
        last = len(postorder) - 1

        """create hashmap for idx and val for inorder"""
        inordermap = {val: idx for idx, val in enumerate(inorder)}

        return self.helper(last, 0, len(inorder) - 1, inordermap, postorder)
