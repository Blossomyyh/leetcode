from typing import List

"""
238. Product of Array Except Self

go through the array in a single path and we start multiply those products together
get the product from all the elements
traversal 1 more this product/its own num


"""
class Solution(object):
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [1]*len(nums)
        product = 1
        """start forom 1- end"""
        for i in range(1, len(nums)):
            # multiple i-1 on right
            product *= nums[i-1]
            right[i]= product
        product = 1
        # range len-2 to 0
        for i in range(len(nums)-2, -1, -1):
            # multiple i+1 on left
            product *= nums[i+1]
            right[i] *= product
        return right
print(Solution().productExceptSelf([1,2,3,4]))
