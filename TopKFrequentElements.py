# heap is partially sorted
# to give a refresher about what heap are, they are like binary trees essentially3
# and you have top most element being the maximum or minimum number however you decided to sort the heap
# and every element under that will be is going to be lesser in value
# but not entirely sorted, if you were to pop off every element from the heap and remove each item then you should sort that way

# pop off n element, each time you need to reset the heap and bubble things up -> make next highest number the top of the heap

import heapq
from typing import List
from collections import defaultdict
from collections import Counter
"""
If two words have the same frequency, then the word with the
 lower alphabetical order comes first.
"""
class Solution(object):
    """not only sorted by frequency but also the alphbetically of the words"""

    def topKFrequentwithHeap(self, nums, k):
        counter = defaultdict(int)
        for n in nums:
            counter[n] = counter.get(n, 0) +1
    #     heap to get top k --> max k
        heap = []
        for num, fre in counter.items():
            heap.append((-fre, num))
        heapq.heapify(heap)

        res  = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res



    def topK(self, nums, k):
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        dlist = list(dic.items())
        dlist.sort(key=lambda x: -x[0], reverse= True)
        return heapq.nlargest(k, dic, key=dic.get)

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """use counter"""
        counter = Counter(words)
        #         counter.items(all two), counter.values() & counter.keys()
        heap = [(-fre, word) for word, fre in counter.items()]
        #     wanna make top most ele to be the maximum, so use -fre,
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


    # You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for x in words:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        res = sorted(d.keys(), key=lambda w: (-d[w], w))
        return res[:k]

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)
        for w in words:
            d[w] += 1
        dlist = list(d.items())
        list.sort(dlist, key=lambda x: (-x[1], x[0]), reverse=True)
        # in dlist 1-word 2-fre, -x[1] reverse, x[0] noreverse
        # reverse true--> from high to low
        return [word for word, count in dlist[-k:][::-1]]

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)
        for w in words:
            d[w] += 1
        dlist = list(d.items())
        list.sort(dlist, key=lambda x: (-x[1], x[0]))
        # sort with 0 down highest to lowest and 1 reverse
        print(dlist)
        # [('i', 2), ('love', 2), ('coding', 1), ('leetcode', 1)]
        print(dlist[::-1])
        # [('leetcode', 1), ('coding', 1), ('love', 2), ('i', 2)]
        return [word for word, count in dlist[:k]]

print(Solution().topKFrequentwithHeap([1,1,1,2,2,3], 2))





"""subtree"""
class Node:
    def __init__(self, val=None):
        self.val = val
        self.childs = []


def dfs(node, cache):
    if not node:
        return 0

    for c in node.childs:
        cache[node.val].extend(dfs(c, cache))
    cache[node.val].extend([node.val])

    return cache[node.val]


def solution(node):
    import collections
    cache = collections.defaultdict(list)
    dfs(n, cache)

    maxx = float('-inf')
    result = None

    for item in cache:
        if len(cache[item]) > 1:
            val = sum(cache[item]) / len(cache[item])

            if val > maxx:
                result = item
                maxx = val
    return result


# Testcase
# n = Node(20)
# n12 = Node(12)
# n12.childs = [Node(11), Node(2), Node(3)]
# n18 = Node(18)
# n18.childs = [Node(15), Node(8)]
#
# n.childs = [n12, n18]
#
# solution(n)