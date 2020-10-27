# Heap, O(nlgk)
from typing import List
from heapq import heappush, heappop


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            heappush(heap, (-self.dis(point), point))
            if len(heap) > K:
                heappop(heap)
        return [i[1] for i in heap]

    def dis(self, point):
        return point[0] * point[0] + point[1] * point[1]

# Quick
# Select, O(n)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        index = self.findK(points, K, 0, len(points) - 1)
        return points[:index + 1]

    def findK(self, arr, K, start, end):
        if start >= end:
            return start
        left, right = start, end
        target = arr[(left + right) // 2]
        while left <= right:
            while left <= right and self.smaller(arr[left], target):
                left += 1
            while left <= right and self.smaller(target, arr[right]):
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        if start + K - 1 <= right:
            return self.findK(arr, K, start, right)
        if start + K - 1 >= left:
            return self.findK(arr, K - (left - start), left, end)
        return right + 1

    def smaller(self, a1, a2):
        return self.dis(a1) < self.dis(a2)

    def dis(self, a):
        return a[0] * a[0] + a[1] * a[1]