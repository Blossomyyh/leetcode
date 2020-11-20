"""
TOPOLOGICAL SORT
1. check can sort topologically -- use set(true/false) -- mmet before?? to check whether have cycle by dfs
2. foundamental - graph + indegree

create a list to store sort result
build a graph(dictionary) key - prerequest, value - courses
indegree dic for each ele - store the number of pre
BFS - go through all courses in the same level
use queue to implement, add all courses without any pre
while queue not empty:
     pop out first one add to the list
     push all related coursed into queue
    // exception
    the course should not be visited before or there's a loop

"""
# cycle
t = [("A", "C"), ("C", "A"),("B", "D"), ("D", "A"), ("G", "E"), ("E", "B")]
#  no cycle
test1 = [("A", "C"), ("B", "D"), ("D", "A"), ("G", "E"), ("E", "B")]

"""
Assumptions: assume there's no duplication in the list
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.


###################################################

1. input = list , output = sorted string

BFS/DFS traversal + topological sort

\\ Exceptions:
    cycle -- \\ 1. len(result) != num of ele
             \\ 2. visited edges != len(input)
             
"""
from collections import defaultdict
from collections import deque
def topological(test):
    def buildGraph(test):
        dic = defaultdict(list)
        indegree = defaultdict(int)
        for pre, course in test:
            dic[pre].append(course)
            # add course into key
            indegree[course] = indegree.get(course, 0) + 1
            # add pre into key
            if pre not in indegree:
                indegree[pre] = 0

        return dic, indegree

    graph, indegree = buildGraph(test)
    # print(graph)
    # print(indegree)

    # first with 0 degree node
    queue = deque()
    for i in indegree:
        if indegree[i] == 0:
            queue.append(i)

    sortList = []
    while queue:
        node = queue.popleft()
        sortList.append(node)
        for n in graph[node]:
            indegree[n] -= 1
            if indegree[n] == 0:
                queue.append(n)
    # print(sortList)
    # print(indegree)
    if len(sortList) == len(indegree):
        return "".join(sortList)
    return []
# print(topological(t))
# print(topological(test1))


"""
######################################
1. input string list, output --> MID of each path

string -> pair : combination
BFS traversal + topo store all path in list
return the middle of each sublist
"""
def topologicalCom(test):
    def buildGraph(test):
        dic = defaultdict(list)
        indegree = defaultdict(int)
        for pre, course in test:
            dic[pre].append(course)
            indegree[course] = indegree.get(course, 0) + 1
            if pre not in indegree:
                indegree[pre] = 0

        return dic, indegree

    testList = []
    # permutationj
    """
    \\ string bca --> bc, ba, ca 
    """
    for string in test:
        for i in range(len(string)):
            for j in range(i+1, len(string)):
                testList.append([string[i], string[j]])
    print(testList)

    graph, indegree = buildGraph(testList)
    print(graph)
    print(indegree)

    # first with 0 degree node
    queue = deque()
    for i in indegree:
        if indegree[i] == 0:
            queue.append(i)

    sortList = []
    while queue:
        node = queue.popleft()
        sortList.append(node)
        for n in graph[node]:
            indegree[n] -= 1
            if indegree[n] == 0:
                queue.append(n)

    print(sortList)
    print(indegree)
    """
    ########################
    return Middle of list:
       \\ %2 == 1: [ len//2 ] 
       \\ %2 == 0: [ len//2 -1 ]
    
    """
    if len(sortList) == len(indegree):
        return sortList[len(sortList)//2] if len(sortList)%2 == 1 else sortList[len(sortList)//2-1]
    return []

print(topologicalCom(['bca', 'be', 'ec']))

"""
###############
3. Get all the path topologicallly

DFS traversal 
"""
def topologicalCom(test):

    def buildGraph(test):
        dic = defaultdict(list)
        indegree = defaultdict(int)
        for pre, course in test:
            dic[pre].append(course)
            indegree[course] = indegree.get(course, 0) + 1
            if pre not in indegree:
                indegree[pre] = 0
        return dic, indegree

    graph, indegree = buildGraph(test)
    print(graph)
    print(indegree)

    # first with 0 degree node
    stack = []

    result = []
    def dfsAllPath(path):
        node = stack.pop()
        if len(graph[node])==0:
            result.append(path+[node])
            return
        for ele in graph[node]:
            stack.append(ele)
            dfsAllPath(path + [node])

    for ele in indegree:
        if indegree[ele] == 0:
            stack.append(ele)
            dfsAllPath([])
    print(stack)
    print(result)
    print(indegree)
    """
    ########################
    return Middle of list:
       \\ %2 == 1: [ len//2 ] 
       \\ %2 == 0: [ len//2 -1 ]

    """
    resultMid = set()
    for singlepath in result:
        if len(singlepath)%2 == 1:
            resultMid.add(singlepath[len(singlepath)//2])
        else:
            resultMid.add(singlepath[len(singlepath)//2-1])
    return list(resultMid)


print(topologicalCom([("A", "B"), ("B", "D"), ("E", "B"), ("E", "C"), ("C", "F"), ("E", "F")]))

def find_mid_topo(courses):
    graph = build_graph(courses)
    indegree = build_indegree(graph)
    print(graph)
    print(indegree)

    from collections import deque
    q = deque()

    for k in indegree:
        if indegree[k] == 0:
            q.append(k)

    topo = ""
    while q:
        cur_course = q.popleft()
        topo += cur_course
        for nei in graph[cur_course]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    print(topo)

    if len(topo) % 2 == 1:
        return topo[len(topo) // 2]
    else:
        return topo[len(topo) // 2 - 1]


def build_graph(courses):
    graph = {}
    for a, b in courses:
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()

        graph[a].add(b)
    return graph


def build_indegree(graph):
    indegree = {k: 0 for k in graph}
    for k in graph:
        for c in graph[k]:
            indegree[c] += 1

    return indegree


print(find_mid_topo(test1))