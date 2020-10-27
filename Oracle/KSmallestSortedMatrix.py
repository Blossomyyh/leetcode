"""


"""

#Here is a 8-liner implementation:
import bisect
class Solution(object):
    def kthSmallest(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo<hi:
            mid = (lo+hi)//2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid+1
            else:
                hi = mid
        return lo
#2. Heap solution gives me 176 ms.
# The time complexity is O(k * log n),
# so the worst-case and average-case time complexity is O(n^2 * log n).
# Space complexity is O(n).

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if j+1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return ret
#3. Sorting gives me 80ms. Time complexity of sorting an array of size n^2 is O(n^2 * log n). Space complexity is O(n^2).

#The difference is that Timsort implemented in Python is capable of taking advantage of existing partial orderings. Moving sorted data in bulk is always faster than comparing and moving individual data elements, due to modern hardware architecture. Time complexity is the same because merging n sorted arrays of size n is still O(n^2 * log n) in the worst case.

class Solution(object):
    def kthSmallest(self, matrix, k):
        l = []
        for row in matrix:
            l += row
        return sorted(l)[k-1]