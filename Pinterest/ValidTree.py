"""
261. Graph Valid Tree

Valid tree --> N-1 edges

"""
"""
\\ graph, G, is a tree 
    two conditions are met:

1. G is fully connected. 
    for every pair of nodes in G, there is a path between them.
2. G contains no cycles. 
    there is exactly one path between each pair of nodes in G.
    
\\ Depth-first search is a classic graph-traversal algorithm 
    that can be used to check for both of these conditions:

G is \\ fully connected if, and only if, 
    we started a depth-first search \\ from a single source \\ and discovered \\ all nodes \\ in G during it.
G contains \\ no cycles if, and only if, 
    the depth-first search \\ never goes back to an already discovered node. 
    We need to be careful though not to count trivial cycles of 
    the form A → B → A that occur with most implementations of undirected edges.
"""
"""
\\ DFS from one points -> find all & no cycle ==== graph is fully connected,
\\ edge - \\ N-1 \\ 

false conditions:
    1. extra edge
    2. edge = n-1  but one node no edges
"""
from collections import defaultdict
def validTree(self, n: int, edges: [[int]]) -> bool:
    # only length = n-1 can build tree
    # edges is unique
    if len(edges)!=n-1:
        return False

    # build graph
    # can use set !
    graph = defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for chil in graph[node]:
            dfs(chil)
        return

    dfs(0)
    return len(visited) == n