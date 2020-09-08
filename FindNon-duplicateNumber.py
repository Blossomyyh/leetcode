"""

"""
class Solution(object):
    def findnondup(self, nums):
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, val in count.items():
            if val ==1 :
                return n
        return None

    def singleNumber(self, nums):
        unique = 0
        for n in nums:
            unique ^= n
        return unique


print(Solution().findnondup([4, 3, 2, 4, 1, 3, 2]))
print(Solution().singleNumber([4, 3, 2, 4, 1, 3, 2]))