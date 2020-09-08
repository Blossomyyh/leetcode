"""
665. Non-decreasing Array
do a single path and to see whether it satisfy certain condition
and if you can identify those indices
1. false when we have 2 problem indices
2. one problem area:
    (1) == 0/len-2 : we change the last/first point and make this work
    (2)another edge cases like if you just play around you will see
    if next 2 is greater than cur problem index -- just change the next one to the middle
"""


from typing import List
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        decrease = -1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
#                 get index
                if decrease == -1:
                    decrease = i
                else:
                    return False
        if decrease == -1:
            return True
        elif decrease == 0 or decrease == len(nums) -2:
            return True
        elif decrease< len(nums)-1 and  nums[decrease] <= nums[decrease+2]:
            return True
        elif  nums[decrease-1] <= nums[decrease+1]:
            return True
        return False


print(Solution().checkPossibility([-1,4,2,3]))