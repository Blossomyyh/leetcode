"""
Find Pythagorean Triplets

we can use hashmap to implement it

"""

class Solution(object):
    def findtriplets(self, nums):
        numSquare = set([n*n for n in nums])
        for a in nums:
            for b in nums:
                if a*a+b*b in numSquare:
                    return True
        return False
print(Solution().findtriplets([3, 5, 12, 5, 13]))