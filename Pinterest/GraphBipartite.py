"""
use a dictionary mark groups for all ele in the list

We should be able to greedily color the graph
if and only if it is bipartite:
one node being blue implies all it's neighbors are red,
all those neighbors are blue, and so on.

for each list in graph:
    for each uncolored ele in list:
        start the coloring process by doing a dfs on that node
        and we let every neighbour colored differently with current node
use a stack to perform dfs --> add uncolored node in it as a todo list...


"""
#  graph record for 0,..n graph[0] means the neighbour of 0
graph = [[1,3], [0,2], [1,3], [0,2]]
graph2 = [[1,2,3], [0,2], [0,1,3], [0,2]]

# DFS solution
def bipartite(graph):
    def dfs(node):
        print(node, dic[node])
        for neighbour in graph[node]:
            if neighbour in dic:
                if dic[neighbour] == dic[node]:

                    return False
                else:
                    continue
            else:
                dic[neighbour] = 1-dic[node]
                print(neighbour, dic[neighbour])
                if not dfs(neighbour):
                    return False
        return True


    dic = {}
    for item in range(len(graph)):
        if item not in dic:
            dic[item] = 0
            if not dfs(item):
                return False
    return True

from collections import deque
def bipartiteBFS(graph):
    color = {}
    queue = deque()
    for node in range(len(graph)):
        if node not in color:
            color[node] = 0
            queue.append(node)
            while queue:
                n = queue.popleft()
                for neighbour in graph[n]:
                    if neighbour in color:
                        if color[neighbour] == color[n]:
                            return False
                        else:
                            continue
                    else:
                        color[neighbour] = 1-color[n]
                        queue.append(neighbour)
    return True

print(bipartiteBFS(graph))
print(bipartiteBFS(graph2))

# BFS solution
def isBipartite(self, graph) -> bool:
    from collections import deque
    queue = deque()
    color = {}
    for i in range(len(graph)):
        if i not in color:
            color[i] = 0
            queue.append(i)
            while queue:
                node = queue.popleft()
                for nb in graph[node]:
                    if nb in color:
                        if color[nb] == color[node]:
                            return False
                    else:
                        color[nb] = 1 - color[node]
                        queue.append(nb)
    return True

def isBipartite(self, graph) -> bool:
    def dfs_color(i):
        for nb in graph[i]:
            if nb in color:
                if color[nb] == color[i]:
                    return False
            else:
                color[nb] = 1 - color[i]
                if not dfs_color(nb):
                    return False
        return True

    color = {}
    for i in range(len(graph)):
        if i not in color:
            color[i] = 0
            if not dfs_color(i):
                return False
    return True