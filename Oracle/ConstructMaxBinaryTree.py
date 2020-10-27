"""
654. Maximum Binary Tree

recursive
O(n2)
O(n)
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructMaximumBinaryTree(nums) -> TreeNode:
    if not nums or len(nums)==0:
        return None
    rootval = max(nums)
    rootidx = nums.index(rootval)

    root = TreeNode(rootval)
    root.left = constructMaximumBinaryTree(nums[:rootidx])
    root.right = constructMaximumBinaryTree(nums[rootidx+1:])
    return root