class Node(object):
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution(object):
    def _balanced_helper(self, n) -> (bool, int):
        # return isBalanced?, maxheight
        if not n:
            return (0, True)
        leftb, lh = self._balanced_helper(n.left)
        rightb, rh = self._balanced_helper(n.right)
        return ((abs(lh-rh)<=1) and leftb and rightb , max(lh, rh)+1)

    def is_balanced(self, n):
        return self._balanced_helper(n)[0]