'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input:
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

'''
intervals = [[1,3],[2,6],[8,10],[15,18]]
"""
\\ sort the intervals
go single path to merge the overlap:
___
  -
  ---
    --- 

    if prev.end>=cur.start and prev.end<cur.end: 
        prev.end = cur.end
    else if prev.end<cur.start 
        append to result

time ： onlogn
space n
"""
def merge(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort(key=lambda x:(x[0], x[1]))
    result = []
    for interval in intervals:
        if not result:
            result.append(interval)
        else:
            prev = result[-1]
            """
            !!RULE!!   \\>=  \\<
            \\ prev.end >= cur.start & prev.end<cur.end
                    then update end
            \\ prev.end < cur.start
                    then append new
            \\ prev.end > cur.start & prev.end > cur.end
                    ----- do nothing
            """
            if prev[1]>=interval[0] and prev[1]<interval[1]:
                prev[1] = interval[1]
            elif prev[1]<interval[0]:
                result.append(interval)
    return result


"""
\\ 2. connected components
"""
'''
 \\# graph building only for overlapping
build graph for overlapped items store them in a list
    graph[xx] = [x, a ,b]
    (connected mean overlap)
    
\\# record list for connected components
set to record all visited node
dic to record connected components
for each node in intervals
    connected = [] (stack)
    do dfs search at graph start at this node
    while stack:
        if not visited
            append node to dic
            then extend all connected to this stack
return connected components list, number of connected

\\# merge_node
go through each connected list
no need to sort:
    min(start )
    max(end)
'''
import collections
from typing import List
class Solution:
    def overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    def build_graph(self, intervals):
        graph = collections.defaultdict(list)

        for i, interval_i in enumerate(intervals):
            for j in range(i + 1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    graph[tuple(interval_i)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_i)

        return graph

    # merges all of the nodes in this connected component into one interval.
    def merge_nodes(self, nodes):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[1] for node in nodes)
        return [min_start, max_end]

    # gets the connected components of the interval overlap graph.
    def get_components(self, graph, intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp = collections.defaultdict(list)

        def mark_component_dfs(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])

        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if tuple(interval) not in visited:
                mark_component_dfs(interval)
                comp_number += 1

        return nodes_in_comp, comp_number

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = self.build_graph(intervals)
        nodes_in_comp, number_of_comps = self.get_components(graph, intervals)

        # all intervals in each connected component must be merged.
        return [self.merge_nodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
 # {(1, 3): [[2, 6]], (2, 6): [[1, 3]]})
# connected components list {0: [(1, 3), (2, 6)], 1: [(8, 10)], 2: [(15, 18)]}) 3
