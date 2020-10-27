"""



"""
# sort version Nlogn
def calculation(x):
    return x[0] ** 2 + x[1] ** 2
def sortK(points, k):
    points.sort(key=lambda x: calculation(x))
    return points[:k]

import heapq
class Solution:
    def kClosest(self, points, K: int):

        return heapq.nsmallest(K, points, key=lambda i: (i[0]**2 + i[1]**2))
    def useheapify(self, points, K):
        heap = []
        for point in points:
            heap.append((point[0]**2 + point[1]**2, point))

        heapq.heapify(heap)
        res = []
        while K:
            res.append(heapq.heappop(heap)[1])
            K -=1
        return res
print(Solution().useheapify([[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]], 3))


def calcDistance(p):
  return p[0]*p[0] + p[1]*p[1]

def findClosestPoints2(points, k):
  points = sorted(points, key = lambda x: calcDistance(x))
  return points[:k]

def findClosestPoints2(points, k):
  # ( distance, object )
  data = []
  for p in points:
    data.append((calcDistance(p), p))
  heapq.heapify(data)

  result = []
  for i in range(k):
    result.append(heapq.heappop(data)[1])
  return result

print (findClosestPoints2([[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]], 3))