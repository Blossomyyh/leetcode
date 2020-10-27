"""
parent to children

1. get all the parent and children degree 0/1( means node has 0/1 parent)
2. common parent
3. farthest parent


"""
# build a graph - dic to store p - c
# 0 - node not in children set
# 1 - node in result1's children
from collections import defaultdict
def parentChildren(graph):
    if not graph: return [], []
    childParent = defaultdict(list)
    allNode = set()
    for ele in graph:
        parent, child = ele[0], ele[1]
        allNode.add(parent)
        allNode.add(child)
        childParent[child].append(parent)
        if parent not in childParent:
            childParent[parent] = []

    print(childParent)
    #
    # res0 = []
    # for node in allNode:
    #     if len(childParent[node]) ==0:
    #         res0.append(node)
    # res1 = []
    # for node in allNode:
    #     if len(childParent[node])==1:
    #         res1.append(node)

    res0 = [k for k, v in childParent.items() if len(v) == 0]
    res1 = [k for k, v in childParent.items() if len(v) == 1]
    return res0, res1

graph = [[1,4],[1,5],[2,5],[3,6],[6,7],[5,8]]
print(parentChildren(graph))

"""


1   2   3
/\ /    /
4 5    6
   \    /
    8   7
find parent: dfs in the graph until the children has no parent
n1[1,2,3,4]
n2[3,4]
"""
def parentChildren2(graph, n1, n2):
    if not graph: return [], []
    childParent = defaultdict(list)
    allNode = set()
    for ele in graph:
        parent, child = ele[0], ele[1]
        allNode.add(parent)
        allNode.add(child)
        childParent[child].append(parent)
        if parent not in childParent:
            childParent[parent] = []

    print(childParent)
    def findParent(node):
        parentSet = set()
        for p in childParent[node]:
            parentSet.add(p)
            for np in findParent(p):
                parentSet.add(np)
        return list(parentSet)

    pNode1 = findParent(n1)
    pNode2 = findParent(n2)

    for p in pNode1:
        if p in pNode2:
            return True
    return False
print(parentChildren2(graph, 6,7))


def findparent2(graph, node1, node2):
    child_to_parent = {}

    for pair in graph:
        parent = pair[0]
        child = pair[1]

        # make sure dictionary have all node as key
        if parent not in child_to_parent:
            child_to_parent[parent] = []

        child_to_parent[child] = child_to_parent.get(child, []) + [parent]

    from collections import deque
    q = deque(child_to_parent[node1])
    parent_set1 = set()
    while q:
        parent = q.popleft()
        parent_set1.add(parent)
        for grad_parent in child_to_parent[parent]:
            q.append(grad_parent)


    q2 = deque(child_to_parent[node2])
    parent_set2 = set()
    while q2:
        parent = q2.popleft()
        parent_set2.add(parent)
        for grad_parent in child_to_parent[parent]:
            q2.append(grad_parent)
    print(parent_set1)
    print(parent_set2)
    print(parent_set1 & parent_set2)
    return len(parent_set1 & parent_set2) > 0



def parentChildren3(graph, n):
    if not graph: return [], []
    childParent = defaultdict(list)
    allNode = set()
    for ele in graph:
        parent, child = ele[0], ele[1]
        allNode.add(parent)
        allNode.add(child)
        childParent[child].append(parent)
        if parent not in childParent:
            childParent[parent] = []

    print(childParent)

    from collections import deque
    queue = deque([n])
    result  = n
    while queue:
        node = queue.popleft()
        for p in childParent[node]:
            queue.append(p)
            result = p
    print(result)


    def findParent(node):
        parentSet = set()
        for p in childParent[node]:
            parentSet.add(p)
            for np in findParent(p):
                parentSet.add(np)
        return list(parentSet)

    pNode = findParent(n)
    print(pNode)
    return pNode[0]

print(parentChildren3(graph, 8))


def findparent3(graph, node1):
    child_to_parent = {}

    for pair in graph:
        parent = pair[0]
        child = pair[1]

        # make sure dictionary have all node as key
        if parent not in child_to_parent:
            child_to_parent[parent] = []

        child_to_parent[child] = child_to_parent.get(child, []) + [parent]

    from collections import deque

    q = deque(child_to_parent[node1])
    farest = child_to_parent[node1][0]  # initialize
    while q:
        for _ in range(len(q)):
            parent = q.popleft()
            for grad_parent in child_to_parent[parent]:
                q.append(grad_parent)
                farest = grad_parent  # choose first one

    return farest


test1 = [[1, 4], [1, 5], [2, 5], [3, 6], [6, 7], [5, 8]]
print(findparent2(test1, 6, 7))
print(findparent3(test1, 8))