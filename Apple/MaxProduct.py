"""
152. Maximum Product Subarray

Input: [2,3,0,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""

def maxProduct(self, nums: [int]) -> int:
    if not nums:
        return 0
    maxsofar = nums[0]
    minsofar = nums[0]
    res = maxsofar

    """deal with negative & 0 --> minsofar and cur"""

    for i in nums[1:]:
        tempmax = max(i, maxsofar * i, minsofar * i)
        minsofar = min(i, maxsofar * i, minsofar * i)
        maxsofar = tempmax
        res = max(maxsofar, res)
        print(tempmax, minsofar, maxsofar, res)
    return res

"""
While going through numbers in nums, we will have to keep track of the maximum product
 up to that number (we will call max_so_far) and
  minimum product up to that number (we will call min_so_far). 
  The reason behind keeping track of max_so_far is to keep track of the accumulated product of positive numbers. 
  The reason behind keeping track of min_so_far is to properly handle negative numbers.

max_so_far is updated by taking the maximum value among:

1. Current number.
This value will be picked if the accumulated product has been really bad
 (even compared to the current number). 
 This can happen when the current number has a preceding zero 
 (e.g. [0,4]) or is preceded by a single negative number (e.g. [-3,5]).
2. Product of last max_so_far and current number.
This value will be picked if the accumulated product has been steadily increasing
 (all positive numbers).
3. Product of last min_so_far and current number.
This value will be picked if the current number is a negative number and 
the combo chain has been disrupted by a single negative number before
 (In a sense, this value is like an antidote to an already poisoned combo chain).
 
min_so_far is updated in using the same three numbers except 
that we are taking minimum among the above three numbers.
"""