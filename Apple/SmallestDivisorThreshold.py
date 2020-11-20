"""
1283. Find the Smallest Divisor Given a Threshold

Binary search + math.ceil() -- upper bound of div (0.1)->1
"""

"""
\\ if sum > th:  s = mid+1
    else      :  e = mid-1

\\ smallest !! -- left binary search 
    have multiple sum== threshold --> find min one


SOrted List
Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 

"""
import math


class Solution:
    def smallestDivisor(self, nums: [int], threshold: int) -> int:
        if not nums:
            return -1

        def getDiv(div):
            res = 0
            for i in nums:
                res += math.ceil(i / div)
            return res

        start = 1
        end = nums[-1]

        while start <= end:
            mid = (start + end) // 2
            cal = getDiv(mid)
            # print(mid, cal)

            if cal > threshold:
                start = mid + 1
            else:
                end = mid - 1
        return start