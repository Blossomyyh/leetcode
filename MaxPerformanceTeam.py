"""
k size minheap to get k max efficient
Performance = sum(speed) * min(efficiency).
Idea is simple:
try every efficiency value from highest to lowest and
at the same time maintain an as-large-as-possible speed group,
keep adding speed to total speed, if size of engineers group exceeds K,
lay off the engineer with lowest speed.

Sort efficiency with descending order.
    Because, afterwards, when we iterate whole engineers, every round,
    when calculating the current performance,
    minimum efficiency is the effiency of the new incoming engineer.
Maintain a pq to track of the minimum speed in the group.
    If size of group is == K, kick the engineer with minimum speed out
    (since efficiency is fixed by new coming engineer, the only thing matters now is sum of speed).
Calculate/Update performance.
"""
import heapq


class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        heap = []
        spsum, res = 0, 0
        for ef, sp in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(heap, sp)
            spsum += sp
            if len(heap) > k:
                spsum -= heapq.heappop(heap)
            res = max(res, spsum * ef)

        return res % (10 ** 9 + 7)

