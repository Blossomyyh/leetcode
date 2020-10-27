"""
354. Russian Doll Envelopes

You have a number of envelopes with widths and heights given as a pair of integers (w, h)
What is the maximum number of envelopes can you Russian doll? (put one inside other)
Assumption: rotation is not allowed
"""
Input = [[5,4],[6,4],[6,7],[2,3]]
Output = 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

from bisect import bisect_left

'''
\\ sorted the list by ((asc)width, (desc)length)
\\ create new list to store operated envelops
\\ go through unsorted height list:
    find a smaller enve in new list, pop it out
    russsian doll +1
    append our current enve


and we also make sure that when the width is the same,
the envelope with greater height comes first.
Why? This makes sure that when we calculate the LISS, we don't have a case such as [3, 4] [3, 5] (we could increase the LISS but this would be wrong as the width is the same. It can't happen when [3, 5] comes first in the ordering).

n order fix this, we don't just sort increasing in the first dimension - we also sort decreasing on the second dimension, so two envelopes that are equal in the first dimension can never be in the same increasing subsequence.

Now when we sort and extract the second element from the input we get [5, 4, 3, 3], which correctly reflects an LIS of one.
'''
from typing import List

class Solution:
    def maxEnvelopes(self, arr: List[List[int]]) -> int:
        # sort increasing in first dimension and decreasing on second
        #         since we have already make sure the width is sorted with <=
        #           no need to worry about width, the next one should always fit in prev if h>hprv
        arr.sort(key=lambda x: (x[0], -x[1]))
        newList = []
        """ only need to do with hlist, already make sure width is bigger than previous one """
        hlist = [v for _, v in arr]

        for item in hlist:
            if not newList:
                newList.append(item)
            idx = bisect_left(newList, item)
            if idx == len(newList):
                newList.append(item)
            else:
                newList[idx] = item
            print(newList)
        return len(newList)
print(Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))