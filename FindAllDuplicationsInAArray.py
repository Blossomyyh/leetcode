"""
442. Find All Duplicates in an Array

O(1) space and O(N) time complexity
trade off

 some elements appear twice and others appear once.
"""


class Solution(object):
    """use map/ set O(N) O(N)"""
    def findDuplication1(self, nums):
        Set = set()
        output = []
        for n in nums:
            if n in Set:
                output.append(n)
            else:
                Set.add(n)
        return output

    """use sort O(Nlogn) O(1)"""
    def findDuplication2(self, nums):
        output = []
        """sort---> difference between sorted and sort"""
        print(sorted(nums))
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums)-1:
            if nums[i+1] == nums[i]:
                output.append(nums[i])
                i += 2
            else:
                i += 1
        return output


    """ 
    , 1 ≤ a[i] ≤ n (n = size of array),  
    
    time O(n) space O(1)
    """

    # Find all the elements that appear twice
    def findDuplication(self, nums):
        outputs = []
        for n in nums:
            value = abs(n) - 1
            if nums[value] < 0:
                outputs.append(abs(n))
            else:
                nums[value] = - nums[value]
        return outputs


print(Solution().findDuplication([4, 3, 2, 7, 8, 2, 3, 1]))
# [2,3]