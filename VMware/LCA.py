def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    parentval = root.val
    pval = p.val
    qval = q.val
    if pval > parentval and qval>parentval:
        # If both p and q are greater than parent
        return lowestCommonAncestor(root.right, p, q)

    # If both p and q are lesser than parent
    elif pval<parentval and qval<parentval:
        return lowestCommonAncestor(root.left, p, q)

        # We have found the split point, i.e. the LCA node.

    else:
        return root


    """
    Start traversing the tree from the root node.
If both the nodes p and q are in the right subtree, then continue the search with right subtree starting step 1.
If both the nodes p and q are in the left subtree, then continue the search with left subtree starting step 1.
If both step 2 and step 3 are not true, this means we have found the node which is common to node p's and q's subtrees. and hence we return this common node as the LCA.

    
    """


""""""


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # top root; pis ancestor, q
    def recurse_tree(current_node):

        # If reached the end of a branch, return False.
        if not current_node:
            return False

        # Left Recursion
        left = recurse_tree(current_node.left)

        # Right Recursion
        right = recurse_tree(current_node.right)

        # If the current node is one of p or q
        mid = current_node == p or current_node == q

        # If any two of the three flags left, right or mid become True.
        if mid + left + right >= 2:
            self.ans = current_node

        # Return True if either of the three bool values is True.
        return mid or left or right

    # Traverse the tree
    recurse_tree(root)
    return self.ans
""""""

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
        node = stack.pop()
        # While traversing the tree, keep saving the parent pointers.
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    ancestor = set()
    while p:
        ancestor.add(p)
        p = parent[p]

    while q not in ancestor:
        q = parent[q]
    return q

