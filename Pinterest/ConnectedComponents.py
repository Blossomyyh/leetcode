"""
323. Number of Connected Components in an Undirected Graph
"""
"""
use dfs - stack to traversal all connected ones
count groups by iteration
"""

from collections import defaultdict
def countComponents(self, n: int, edges: [[int]]) -> int:
    # build graph
    graph = defaultdict(set)
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    visited = set()
    connected = defaultdict(list)

    def dfs(node, idx):
        stack = [node]
        while stack:
            cur = stack.pop()
            if cur not in visited:
                visited.add(cur)
                connected[idx].append(cur)
                for adj in graph[cur]:
                    stack.append(adj)

    count = 0
    for i in range(n):
        if i not in visited:
            dfs(i, count)
            count += 1
    return count