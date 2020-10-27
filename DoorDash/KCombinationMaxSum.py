import heapq


def find_K_max_sum(arr1, arr2, K):
    arr1.sort()
    arr2.sort()

    i = len(arr1) - 1
    j = len(arr2) - 1
    heap = []
    heapq.heappush(heap, (-(arr1[i] + arr2[j]), i, j))
    res = []
    index_set = set([(i, j)])

    count = 0
    while count < K:
        val, i, j = heapq.heappop(heap)
        count += 1
        res.append((arr1[i], arr2[j]))

        if i > 0 and j - 1 > 0:
            if (i, j - 1) not in index_set:
                heapq.heappush(heap, (-(arr1[i] + arr2[j - 1]), i, j - 1))
                index_set.add((i, j - 1))
        if i - 1 > 0 and j > 0:
            if (i - 1, j) not in index_set:
                heapq.heappush(heap, (-(arr1[i - 1] + arr2[j]), i - 1, j))
                index_set.add((i - 1, j))

    # for _ in range(K):
    #     val, i, j = heapq.heappop(heap)
    #     print(i, j)
    #     res.append((arr1[i], arr2[j]))

    #     if i > 0 and j - 1 > 0:
    #         heapq.heappush(heap, (-(arr1[i] + arr2[j-1]), i, j-1))
    #     if i - 1 > 0 and j > 0:
    #         heapq.heappush(heap, (-(arr1[i-1] + arr2[j]), i-1, j))

    print(arr1, arr2)
    print(res)
    return res


find_K_max_sum([2, 3, -1, 0, 5], [1, 4, 2], 8)