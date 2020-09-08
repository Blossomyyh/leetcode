"""
1560. Most Visited Sector in a Circular Track

Given an integer n and an integer array rounds.
We have a circular track which consists of n sectors labeled from 1 to n.
A marathon will be held on this track,
 the marathon consists of m rounds. The ith round starts at sector rounds[i - 1]
 and ends at sector rounds[i]. For example, round 1 starts at sector rounds[0]
 and ends at sector rounds[1]

Return an array of the most visited sectors sorted in ascending order.

"""

from collections import Counter
from typing import List
class Solution:
    def nextSector(self, n: int, i: int):
        if i < n:
            return i+1
        else:
            return 1

    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        count = Counter()

        for i in range(1, len(rounds)):
            e = rounds[i]
            s = rounds[i - 1] if i == 1 else self.nextSector(n, rounds[i - 1])
            for j in range(n):
                count[s] += 1
                s = self.nextSector(n, s)
                if s == e:
                    break
        fredic = count.most_common()
        """ most_common will return all elements with frequency ordered"""
        print(fredic)
        tf = fredic[0][1]
        """
        first need get tf--most frequency
        than filter with ele only has tf
        map this tuple and only get [0]
        then sorted the ele
        """
        return sorted(map(lambda x: x[0], filter(lambda t: t[1]==tf, fredic)))
print(Solution().mostVisited(4,[1,3,1,2]))