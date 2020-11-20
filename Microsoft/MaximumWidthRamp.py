"""
962. Maximum Width Ramp

Given an array A of integers,
 a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].
  The width of such a ramp is j - i.

Time Complexity: O(NlogN), where NN is the length of A.
Space Complexity: O(N), depending on the implementation of the sorting function.

"""
"""
\\ sol 1 : sort the index by key -- according value in the list
"""
import bisect

class Solution:
    def maxWidthRamp(self, A:[int]) -> int:
        ans = 0
        m = float('inf')
        l = [i for i in range(len(A))]
        l.sort(key=A.__getitem__)
        # print(l)
        for i in l:
            ans = max(ans, i - m)
            m = min(m, i)
        return ans

    """
    \\ sol 2 : binary search for each element
    """

    """
        Consider i in decreasing order. 
        We want to find the largest j with A[j] >= A[i] if it exists.
        
        1. reversely traversal A  (make sure get the bigger and father one)
        2. use list to store (value, idx)
        3. check insert position:
            == len
                append to end of the list
            < len
                update answer
                
    """

    def maxWidthRamp(self, A: [int]) -> int:
        ans = 0
        candidate = [(A[-1], len(A) - 1)]
        for idx in range(len(A) - 2, -1, -1):
            a = A[idx]
            insert = bisect.bisect_left(candidate, (a,))
            if insert < len(candidate):
                ans = max(ans, candidate[insert][1] - idx)
            else:
                candidate.insert(insert, (a, idx))
                # print(candidate)
        return ans

    """
    \\ sol 3
    ntuition:
    Keep a decraesing stack.
    For each number,
    binary search the first smaller number in the stack.
    
    When the number is smaller than the last,
    push it into the stack.
    
    Time Complexity:
    O(NlogN)
    """

Solution().maxWidthRamp([6,0,8,2,1,5])