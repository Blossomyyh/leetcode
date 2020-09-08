"""
46 permutations

first of all there is no efficient way to do it
it has to be brute force
we're just going to generate every single combination
let's take look at this one

[1,2,3]
you have 3 spots
and the first element/ scenario  you can have up to 3 different numbers
second - 2, last position - only one number
this is known as *factorial*
then it's like N times N minus 1 times N-2 ... until you get to one

we gonna do here is use backtracking
traversal this path and get the combination
then we have to go back and try
first and another branch and go back to the top and go down to the next value
likewise go up and down

so the code to write this out is that you just do an iteration
So we need to take just one of the values and then remove that
from the set of potential candidates for the next iteration

for.....   one way we can do this is we could swap a value -- perform swap, right?
swap(start, i) and swap the index at, say the start index and index of i
and then we just call f(n) again, and we pass the start and the index + 1 right?
so we move the start index up by 1.
and then at the end of that, we swap it back.

that's pretty much what the algorithms looks like in pseudo-code
you just go through each element, transfer up into the front
and then you need to call[f(n)] for the subsequent elements, processing the rest of the array
tying to swap those elements and then for the base case, you would say,
if ever the start index equals the end, so you reach the end of the array, then you found one combination and you are just
return the array you have

so the return value of this is going to be an array of these numbers.
"""


class Solution:
    # swap / get list / swap
    # backtracking
    """ distinct integers"""
    """interation version"""
    def permutationHelper(self, nums, start=0):
        if start == len(nums) - 1:
            return [nums[:]]
        res = []
        for i in range(start, len(nums)):
            # self.swap(nums, start, i)
            nums[start], nums[i] = nums[i], nums[start]
            res += self.permutationHelper(nums, start + 1)
            nums[start], nums[i] = nums[i], nums[start]
        return res

    def permutation1(self, nums):
        return self.permutationHelper(nums, 0)

    """
    choose from left numbers
    """
    # principle is pretty similar but for this, you pass in the numbers that are valid for use
    # then you constructing this value array that you go through

    """iteration version"""
    def permutation1noswap(self, nums, values=[]):
        if not nums:
            return [values]
        res = []
        for i in range(len(nums)):
            res += self.permutation1noswap(nums[:i] + nums[i+1:],values + [nums[i]] )
        return res

    """recursive version"""
    def permutation1noswaprec(self, nums):
        res = []
        stack = [(nums, [])]
        while(len(stack)):
            nums, values = stack.pop()
            if not nums:
                res += [values]
            """range(len(nums)) not nums!!!!"""
            for i in range(len(nums)):
                stack.append((nums[:i]+nums[i+1:], values + [nums[i]]))
        return res




print(  Solution().permutation1noswaprec([1, 2, 3]))

