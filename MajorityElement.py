from typing import List
from bisect import bisect_left, bisect_right
# Majority Element
#  which is defined as one group being greater than any other in the set. >= 1/2
# Using Binary Search, find the first and last occurrences of A. 
# Then just calculate the difference between the indexes of these occurrences.
def isMajorityElement(nums: List[int], target: int) -> bool:
    i = bisect_left(nums, target)
    j = bisect_right(nums,target)
    return (j - i)>len(nums)//2


print(isMajorityElement([1,2,2,2,3], 2))