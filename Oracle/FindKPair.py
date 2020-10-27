"""
532. K-diff Pairs in an Array


sol 1: 2 pointer
fast and slow - 1 & 0

"""
def findPairs(self, nums, k: int) -> int:
    nums.sort()
    slow = 0
    fast = 1
    res = 0
    while slow < len(nums) and fast < len(nums):
        if slow == fast or nums[slow] + k > nums[fast]:
            fast += 1
        elif nums[slow] + k < nums[fast]:
            slow += 1
        else:
            res += 1
            slow += 1
            while (slow < len(nums) and nums[slow] == nums[slow - 1]):
                slow += 1

    return res


'''
\\ sol 2: use hashmap
Time complexity : O(N)
Space complexity : O(N)
'''
from collections import Counter

class Solution:
    def findPairs(self, nums, k):
        result = 0

        counter = Counter(nums)

        for x in counter:
            if k > 0 and x + k in counter:
                result += 1
            elif k == 0 and counter[x] > 1:
                result += 1
        return result