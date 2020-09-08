"""
Sorting a list with 3 unique numbers

inputs [2,3,1,2,3,2,1]
outputs [1,1,2,2,2,3,3]

1. sort it - quick(worst case n^2, choose to pivot poorly)/merge sort
2. one single path - linear time using a hash map

!3. sort in place and linear
keep track of 2 pointers start & end
anytime see 1, swap it with start++
anytime see 3, swap it with end--
"""

class Solution():
    """in space"""
    def sortwith3unique(self, nums):
        start  = 0
        end = len(nums)-1
        i = 0
        while i <= end:
            if nums[i]== 1:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
                i += 1
            elif nums[i] == 3:
                """no need to i++ since after swap, it may change to 1/2"""
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
            elif nums[i] == 2:
                i += 1
        return nums


    def withHashmap(self, nums):
        dic = {}
        for n in nums:
            dic[n]  = dic.get(n, 0) + 1

        return ([1] * dic.get(1, 0) +
                [2] * dic.get(2, 0) +
                [3] * dic.get(3, 0))

print(Solution().sortwith3unique([3, 3, 2, 1, 3, 2, 1]))
print(Solution().withHashmap([3, 3, 2, 1, 3, 2, 1]))