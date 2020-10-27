"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

EX 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.

"""

"""only check cycles"""
from typing import List
from collections import defaultdict, deque


class Solution:
    """solution 1: backtracking"""
    """
    graph traversal problem, where each course can be represented as a vertex in a graph 
    and the dependency between the courses can be modeled as a directed edge between two vertex.

     satisfies all the dependencies (i.e. constraints) would be equivalent to determine 
     if the corresponding graph is a DAG (Directed Acyclic Graph), 
     i.e. there is no cycle existed in the graph.

      would be backtracking or simply DFS (depth-first search).
      The check of cyclic dependencies for each course could be done via backtracking, where we incrementally follow the dependencies until either there is no more dependency or we come across a previously visited course along the path.

      dfs， remember adjecent nodes along the path, if there is no adjecent nodes, then

    """

    def checkCycle(self, course, dic, visited):
        #     dfs
        if visited[course]:
            return True
        visited[course] = True
        # backtracking
        res = False
        for pre in dic[course]:
            res = self.checkCycle(pre, dic, visited)
            if res: break
        # after backtracking, remove the node from the path
        visited[course] = False
        return res

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        for course, pre in prerequisites:
            #             should record according to graph: 0-> 1, 1->0 (0,1 is prerequest)
            dic[pre].append(course)
        visited = [False] * numCourses
        # visited is to remember each vector we go through
        #         dic may change size -> have some course 1->[], it will appear during call out
        for course in range(numCourses):
            if self.checkCycle(course, dic, visited):
                return False
        return True

    """
    backtracking 
    space - o[n], time o[v^2+e]
     |E|∣E∣ is the number of dependencies, 
     |V|∣V∣ is the number of courses and d is the maximum length of acyclic paths in the graph.
    """

    """ postorder DFS """
    """
    check the current node at last and use checked to remember whether the road has been checked before!
    """

    def checkCycle2(self, course, dic, checked, visited):
        #  post   dfs
        if checked[course]:
            return False
        if visited[course]:
            return True

        visited[course] = True
        # backtracking
        res = False
        for pre in dic[course]:
            res = self.checkCycle2(pre, dic, checked, visited)
            if res: break
        # after backtracking, remove the node from the path
        visited[course] = False
        checked[course] = True
        # visited means grey node, not fully visited; checked means black nodes, has been visited all the adjecent node
        return res

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        for course, pre in prerequisites:
            #             should record according to graph: 0-> 1, 1->0 (0,1 is prerequest)
            dic[pre].append(course)
        # approve the path of numcourse has no cycle
        visited = [False] * numCourses
        # approve whether the cycle checked before
        checked = [False] * numCourses
        #         dic may change size -> have some course 1->[], it will appear during call out
        for course in range(numCourses):
            if self.checkCycle2(course, dic, checked, visited):
                return False
        return True

    """
    post order DFS
    use another checked to remember 
    ?Note, one could also use a single bitmap with 3 states such as not_visited, visited, checked, 
    rather than having two bitmaps as we did in the algorithm, though we argue that it might be clearer to have two separated bitmaps.
    
    Time Complexity: \mathcal{O}(|E| + |V|)O(∣E∣+∣V∣) 
    where |V|∣V∣ is the number of courses, and |E|∣E∣ is the number of dependencies.
     a postorder DFS traversal in the graph,
      we visit each vertex and each edge once and only once in the worst case
      
    Space Complexity: \mathcal{O}(|E| + |V|)O(∣E∣+∣V∣), 
      with the same denotation as in the above time complexity.
      we employed two bitmaps (path and visited) to keep track of the 
      visited path and the status of check respectively, which consumes  |V|2⋅∣V∣ space.
       function in recursion, which would incur additional memory consumption on call stack.
        In the worst case where all nodes chained up in a line, the recursion would pile up |V|∣V∣ times.
    """


Solution().canFinish(2, [[0, 1]])

"""best answer"""
"""
input: graph
output: bool - whether it has cycle
go dfs, check whether we may meet some nodes we visited before
states for each node - visiting/ done(into queue)

for all vertex in graph:
    if v is done visiting, we can move on 
    if not mark v as visiting
    we find its adjacent list in graph
    for each neighbour in adjacent list:
        do check n again recursively
            dfs helper: check whether the node is visited before if not mark as visiting
            if cycle , stop and return True
    after mark all neighbour for this node, we mark this vertex as done
return false for no cycle
"""


class Graph:
    def __init__(self):
        self.edges = {}

    def add_edges(self, start_node, end_node):
        if start_node not in self.edges:
            self.edges[start_node] = []
        if end_node not in self.edges:
            self.edges[end_node] = []
        self.edges[start_node].append(end_node)


# 2 state for vertex
VISITING = 0
DONE = 1


def has_cycle(graph):
    visited = {}
    for vertex in graph.edges:
        # do dfs for each vertex
        if cycle_helper(vertex, graph, visited):
            return True
    return False


def cycle_helper(vertex, graph, visited):
    if vertex in visited and visited[vertex] == DONE:
        return False
    else:
        visited[vertex] = VISITING
        for neighbour in graph.edges[vertex]:
            # check neighbour status right here, return cycle if find neighbour is visiting
            if neighbour in visited:
                if visited[neighbour] == VISITING:
                    return True
                elif visited[neighbour] == DONE:
                    continue
            else:
                if cycle_helper(neighbour, graph, visited):
                    return True
                visited[neighbour] = DONE
    return False


graph = Graph()
graph.add_edges(1, 2)
graph.add_edges(1, 3)
graph.add_edges(3, 2)
graph.add_edges(5, 2)
graph.add_edges(4, 2)

print(has_cycle(graph))





"""Topological sort"""

class Topological(object):
    """Topological sort - DAG"""
    """
    L = Empty list that will contain the sorted elements
    S = Set of all nodes with no incoming edge
    
    while S is non-empty do
        remove a node n from S
        add n to tail of L
        for each node m with an edge e from n to m do
            remove edge e from the graph
            if m has no other incoming edges then
                insert m into S
    
    if graph has edges then
        return error   (graph has at least one cycle)
    else 
        return L   (a topologically sorted order)
    """

    """
    use indegree to find the order and DAG
    
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacent_list = defaultdict(list)
        vertex_indegree = defaultdict(int)
        topology = []

        for course, prerequisite in prerequisites:
            adjacent_list[prerequisite].append(course)
            vertex_indegree[course] = vertex_indegree.get(course, 0) + 1

        """first initialize a queue with 0 in-degree(those courses!)"""
        # Queue for maintainig list of nodes that have 0 in-degree
        queue = deque([k for k in range(numCourses) if k not in vertex_indegree])

        while queue:
            vertex = queue.popleft()
            topology.append(vertex)

            if vertex in adjacent_list:
                for neighbour in adjacent_list[vertex]:
                    vertex_indegree[neighbour] -= 1
                    if vertex_indegree[neighbour] == 0:
                        queue.append(neighbour)
        return topology if len(topology) == numCourses else []


# Test
# Cases:
#
# Empty /
#
# BasicCanFinishFalse
# courseNum = 2, [[0, 1], [1, 0]]
#
# BasicCanFinishTrue
# courseNum = 3, [[0, 1], [1, 2]]



######################
"""
half way of course path
 
"""
