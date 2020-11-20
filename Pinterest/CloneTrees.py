class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

def findNode(a, b, node):
    if a==node:
        return b
    if a.left and b.left:
        found = findNode(a.left, b.left, node)
        if found:
            return found
    if a.right and b.right:
        found = findNode(a.right, b.right, node)
        if found:
            return found
    return None
def findNode2(a, b, node):
    stack = [(a, b)]
    while stack:
        (cura, curb) = stack.pop()
        if cura == node:
            return b
        if a.left and b.left:
            stack.append((a.left, b.left))
        if b.right and b.right:
            stack.append((a.right, a.right))
    return None