"""
297. Serialize and Deserialize Binary Tree
encode and decode

preorder to decode
"""
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        res = ""
        res += str(self.val)
        if self.left:
            res += str(self.left)
        if self.right:
            res += str(self.right)
        return res

class solution:
    def serialize(self, node):
        if node == None:
            return "#"
        return str(node.val) + " " + self.serialize(node.left)+" "+self.serialize(node.right)

    def deserialize(self, string):
        strnodes = string.split(' ')
        self.idx = 0
        def helper(idx):
            if strnodes[idx] == '#':
                self.idx += 1
                return None
            root = Node(int(strnodes[idx]))
            self.idx += 1
            root.left = helper(self.idx)
            root.right = helper(self.idx)
            return root
        return helper(self.idx)
tree = Node(1)
tree.left = Node(3)
tree.right = Node(4)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right.right = Node(7)
# 132547
s = solution().serialize(tree)
print(s)
n = solution().deserialize(s)
print(n)



def serialize(node):
  if node == None:
    return '#'
  return str(node.val) + ' ' + serialize(node.left) + ' ' + serialize(node.right)
# 132##5##4#7##

def deserialize(str):
  def deserialize_helper(values):
    value = next(values)
    if value == '#':
      return None
    node = Node(int(value))
    node.left = deserialize_helper(values)
    node.right = deserialize_helper(values)
    return node
  values = iter(str.split())
  print(str.split())
  return deserialize_helper(values)
#      1
#     / \
#    3   4
#   / \   \
#  2   5   7
tree = Node(1)
tree.left = Node(3)
tree.right = Node(4)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right.right = Node(7)
string = serialize(tree)
print(deserialize(string))
# 132547