"""
340. Longest Substring with At Most K Distinct Characters

"""
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s, k):

        dic = defaultdict(int)
        low = 0
        res = 0
        for idx, i in enumerate(s):
            dic[i] = idx
            if len(dic)>k:
                low = min(dic.values())
                del dic[s[low]]
                low += 1
            res = max(res, idx - low + 1)
        return res


"""
Time complexity : O(N) 
in the best case of k distinct characters in the string and 
O(Nk) in the worst case of N distinct characters in the string.

Space complexity : O(k) 
since additional space is used only for a hashmap with at most k + 1 elements.
"""


"""
\\ sol 2 -- ordered dictionary
"""