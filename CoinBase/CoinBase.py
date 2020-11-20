import math

# Complete the 'minimumDivisor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER threshold
#
def minimumDivisor(arr, threshold):
    def calculate(i):
        res = 0
        for n in arr:
            res += math.ceil(n / i)
        return res

    s, e = 1, max(arr)
    while s < e:
        m = (s + e) // 2
        cal = calculate(m)
        if cal > threshold:
            s = m + 1
        else:
            e = m
    return s

print(minimumDivisor([2,3,5], 10))

# Complete the 'segment' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER_ARRAY space
#
import heapq


def segment(x, space):
    heap = []
    for i in range(x):
        heapq.heappush(heap, (space[i], i))
    heapq.heapify(heap)
    res = heap[0][0]

    for i in range(x, len(space)):
        heapq.heappush(heap, (space[i], i))
        while heap and heap[0][1] <= i - x:
            heapq.heappop(heap)
        res = max(heap[0][0], res)
    return res