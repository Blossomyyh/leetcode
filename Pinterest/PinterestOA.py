"""
1.domain
2.mergeInterval
3.

"""


from typing import List
import collections
"""
1. domain
811. Subdomain Visit Count

deal with string
init a dictionary to store all domains and counts accordingly
split each string to get count and whole domain name-> split to subdomain
add counts to dictionary
output dictionary
"""
def subdomainVisits(cpdomains: List[str]) -> List[str]:
    dictionary = {}
    for cpdomain in cpdomains:
        splitString = cpdomain.split(' ')
        count = int(splitString[0])
        domain = splitString[1]
        subdomain = domain.split('.')
        for i in range(len(subdomain)):
            key = ".".join(subdomain[i:])
            dictionary[key] = dictionary.get(key, 0) + count

    result = []
    for key, value in dictionary.items():
        newString = str(value) + " " + key
        result.append(newString)
    return result

# simpler way of domain
def subdomainVisits(cpdomains):
    ans = collections.Counter()
    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)
        frags = domain.split('.')
        for i in range(len(frags)):
            ans[".".join(frags[i:])] += count

    return ["{} {}".format(ct, dom) for dom, ct in ans.items()]

"""
2. Merge Intervals
\\56. Merge Intervals



\\Sol1. use sorting
:exception empty list or len == 1

sort the list by start time
init result list with first interval
go single path, index i from 1 to end:
    compare start[i] with last interval in result:
    if <=: merge -end[i] or previous, change previous end time
    if >: append this interval to result
return list

Assume: the original list can be edited
Time complexity: sort - nlogn - n --> 0(nlogn)
Space - O(1)
"""
def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals or len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        previous = result[-1]
        if intervals[i][0] <= previous[1]:
            previous[1] = max(intervals[i][1], previous[1])
        #     prev_start, prev_end = results[-1]
      # results[-1] = (prev_start, max(prev_end, end))
        else:
            result.append(intervals[i])
    return result
print(merge([[1, 3], [5, 8], [4, 10], [20, 25]]))
# [(1, 3), (4, 10), (20, 25)]

"""
\\Sol2. Connected Components

"""
from collections import defaultdict
class Solution:
    def overlap(self, a, b):
        return a[0]<=b[1] and a[1]>=b[0]
    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    def buildGraph(self, intervals):
        graph = defaultdict(list)
        for i, interval in enumerate(intervals):
            for j in range(i +1, len(intervals)):
                if self.overlap(interval, intervals[j]):
                    # unhashable type: 'list'
                    graph[tuple(interval)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval)

        return graph

    # merges all of the nodes in this connected component into one interval.
    def mergeNodes(self, nodes):
        minStart = min(node[0] for node in nodes)
        maxEnd = max(node[1] for node in nodes)
        return [minStart, maxEnd]

    # gets the connected components of the interval overlap graph.
    def getComponent(self, graph, intervals):
        visited = set()
        compNumber = 0
        nodeComponent = defaultdict(list)

        def markComponentDFS(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodeComponent[compNumber].append(node)
                    stack.extend(graph[node])

        for interval in intervals:
            if tuple(interval) not in visited:
                markComponentDFS(interval)
                compNumber += 1
        return nodeComponent, compNumber

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = self.buildGraph(intervals)
        nodeComponent, number = self.getComponent(graph, intervals)
        result = []
        for component in nodeComponent:
            result.append(self.mergeNodes(nodeComponent[component]))
        return result
print(Solution().merge([[1, 3], [5, 8], [4, 10], [20, 25]]))





