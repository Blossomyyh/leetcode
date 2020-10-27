import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
 return the values of its boundary in anti-clockwise direction starting from root.
"""
class bt:
    def boundaryOfBinaryTree(self, root: TreeNode):
        if not root: return []
        boundary = [root.val]
        def leftmost(node):
            """preorder for left most"""
            if not node or not node.left and not node.right:
                return
            boundary.append(node.val)
            if node.left:
                leftmost(node.left)
            else:
                leftmost(node.right)

        def leaves(node):
            """ inorder for bottom leaves"""
            if not node:
                return
            leaves(node.left)
            if node!=root and not node.left and not node.right:
                boundary.append(node.val)
            leaves(node.right)

        def rightmost(node):
            """postorder for right most"""
            if not node or not node.right and not node.left:
                return
            if node.right:
                rightmost(node.right)
            else:
                rightmost(node.left)
            boundary.append(node.val)

        leftmost(root.left)
        leaves(root)
        rightmost(root.right)
        return boundary


class test(unittest.TestCase):
    def testbt(self):
        """
        test boundaryOfBinaryTree in bt
        :return:
        """
        inputbt = TreeNode(0, TreeNode(2), TreeNode(3))

        res = bt().boundaryOfBinaryTree(inputbt)
        self.assertEqual(res, [0,2,3])



if __name__ == '__main__':
    unittest.main()