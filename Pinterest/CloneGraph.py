"""
deep copy of the graph

initialize a dictionary to pair old node with new one
traversal the tree BFS
1. create queue with [initial root nodes]
2. while loop when queue not empty:
    popleft queue get the cur node
    for neighbour in this old node
        if node not in dic:
            create new node and pair it with old one in dic
            queue append this old node
        new node(pair with old node) append this new children

3. return root


create new nodes on the go
"""

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    def __str__(self):
        print(self.val, self.neighbours)

from collections import deque
class Solution:

    def __init__(self):
        self.visited = set()
    def copyDFS(self, node: Node):
        if not node: return node

        # Create a clone for the given node.
        # Note that we don't have cloned neighbors as of now, hence [].
        newnode = Node(node.val, [])
        # The key is original node and value being the clone node.
        self.visited[node] = newnode

        # Iterate through the neighbors to generate their clones
        # and prepare a list of cloned neighbors to be added to the cloned node.
        for neighbor in node.neighbors:
            # If the node was already visited before.
            # Return the clone from the visited dictionary.

            if neighbor not in self.visited:
                self.cloneGraph(neighbor)
            newnode.neighbors.append(self.visited[neighbor])
        return newnode


    def copyGraph(self, node: Node):
        if not node: return node
        root = Node(node.val, [])
        queue = deque()
        # queue will append nodes -- root nodes may not be only one
        queue.append(node)
        # pair each node with a new node(one child has multiple parents)
        dictionary = {node: root}
        # BFS traversal
        while queue:
            item = queue.popleft()
            for neighbour in item.neighbors:
                if neighbour not in dictionary:
                    newnode = Node(neighbour.val, [])
                    dictionary[neighbour] = newnode

                    queue.append(neighbour)

                dictionary[item].neighbors.append(dictionary[neighbour])
        return root

node = Node(2, [Node(3, []), Node(4, []), Node(5, [Node(1, [])])])

Solution().copyGraph(node)
