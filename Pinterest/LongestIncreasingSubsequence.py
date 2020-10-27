"""
300. Longest Increasing Subsequence
673. Number of Longest Increasing Subsequence
Longest Increasing Subsequence


Given an unsorted array of integers, ﬁnd the length of longest increasing subsequence.
Example:


Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

"""

test1 = [1, 3, 2, 6, 7, 5, 8, 9]
test2 = [1, 3, 2, 2, 6, 7, 7, 5, 8, 9]

# Difference between subsequence & subarray!!!!
#
#  subsequence -- no need to have the same order!
#
# subarray --- same order!!
""" simple Dynamic Programming """
'''
time : O(n^2)
space :O(N)
'''
def longestIncreasingSubstring(string):
    if not string: return 0
    if len(string)==1: return 1
    dp = [0]*len(string)
    ans = 1
    for i in range(len(string)):
        maxnum = 1
        for j in range(i, -1, -1):
            if string[j]<string[i]:
                maxnum = max(maxnum, dp[j])
        dp[i] = maxnum + 1
        ans = max(maxnum, ans)
    return ans

print(longestIncreasingSubstring(test2))

""" Binary search + Dynamic Programming """
'''
time : O(nlogn)
space :O(N)
'''


import bisect
def lisBinary(string):

    # return the idx where var can be insert into the res
    def binary(res, var):
        start = 0
        end = len(res)-1
        while start < end:
            mid = (end + start) // 2
            if res[mid]< var:
                start = mid+1
            else:
                end = mid
        return start


    res = []
    for var in string:
        if not res or res[-1]<var:
            res.append(var)
        else:
            # idx = binary(res, var)
            idx = bisect.bisect_left(res, var, 0, len(res)-1)
            res[idx] = var
        print(res)
    return len(res)

print(lisBinary(test2))


def LIS(arr):
    res = []

    for val in arr:
        if not res or val > res[-1]:
            res.append(val)
        else:
            idx = find_place(res, val)
            res[idx] = val

    return len(res)


def find_place(res, val):
    start, end = 0, len(res) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if res[mid] < val:
            start = mid +1
        else:
            end = mid

    if res[start] >= val:
        return start
    if res[end] >= val:
        return end



print(LIS(test2))



###############################
"""
#####################
Python implementation of 

\\  1. bisect_left(arr, var, lo, hi)

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
        
        
    while lo < hi:
        mid = (lo+hi)//2
        
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo




\\ 2. bisect_right(arr, var, lo, hi)
    
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
        
    while lo < hi:
        mid = (lo+hi)//2
        
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo



\\ 3. bisect
"""


'''
673. Number of Longest Increasing Subsequence
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, 
and there are 5 subsequences' length is 1, so output 5.

'''

###################
"""
Dynamic program
create dp for storing longest length from start to this index
create counts storing numbers of sequence which reaches the longest len

for i and for j less than i
    make sure i<j:
        compare len in dp
            if dp[i]<dp[j]+1:
                inherit len and nums from j to i
                dp[i] = dp[j]+1
                count[i] += count[j]
            else if dp[i]==dp[j]+1:
                count[i] += count[j]
            else:
                continue
traversal dp again, get max len:
    sum up all counts for the max len
return sum
                


"""
from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1
        dp = [1] * len(nums)
        count = [1] * len(nums)
        maxlen = 0
        ans = 0
        for i in range(len(nums)):
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    if dp[i] == dp[j] + 1:
                        count[i] += count[j]
                    elif dp[i] < dp[j] + 1:
                        count[i] = count[j]
                        dp[i] = dp[j] + 1
                    else:
                        continue
            maxlen = max(maxlen, dp[i])
            print(dp[i], count[i])
        print(count)
        print(dp)

        for i in range(len(nums)):
            if dp[i] == maxlen:
                ans += count[i]
        return ans