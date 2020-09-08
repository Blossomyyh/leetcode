# we all know that it's kind of difficult to figure out if a number is prime or not
# that's sort when those problems that are unsolved
# so I don't expect this to have a fantastic runtime
# and I am thinking that it's just going to use a number of heuristics(启发的), right?
# so one thing we can do here is to iterate from 1 to the root of the number,
# that will give us all of the factors
# it will cover everything above that, then we already have covered it from the lower bound
# Once we have all the factors of the number, we just add those up and see if that equals the target number
# so we can try this out
# runtime is going to be square root of k, k the given number
# add it's going to take another pass to add those numbers
# the runtime of that will be the maximum number of factors of a number ,
# at least less than square root of k, which is what are we're bounded by


import math
import functools


class Solution(object):
    # edge checks!!
    def checkPerfectNumber(self, num):
        factors = []
        if num <= 0:
            return False
        """math.ceil() --- Return the ceiling of x, the smallest integer greater than or equal to x."""

        """exponent (**) sign,----- which is used to find out the power of a number."""
        for i in range(1, int(math.ceil(num ** 0.5))):
            # take the mode of each number
            if num % i == 0:
                factors.append(i)
                factors.append(num)
        sum = 0
        if factors:
            # using reduce to ust do a little bit of shorthand
            sum = functools.reduce(lambda x, y: x + y, factors) - num
        return sum == num


# you don't need to do this, but it's just kind of neat and fun to do
# people may appreciate that here and there map reduce filter,
# they can actually save you a little bit of time
# But I would actually warn you against too many tricky things,
#  because later they can be pretty difficult to modify later on
#



import math


class Solution2:
    # define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
    #     the input number n will not exceed 100,000,000. (
    def checkPerfectNumber(self, num: int) -> bool:
        div = []
        if num <= 0: return False
        for i in range(1, int(math.ceil(num ** 0.5))):
            if num % i == 0:
                #                 divisors
                div.append(i)
                # if (num//i) !=num:
                div.append(num // i)
                print(i, num // i)
        return sum(div) - num == num

    def checkPerfectNumberCondition(self, num: int) -> bool:
        sum = 0
        if num <= 0: return False
        for i in range(1, int(math.ceil(num ** 0.5))):
            if num % i == 0:
                #                 divisors
                sum += i
                if (num // i) != num:
                    sum += num // i
                if (sum > num):
                    return False
                print(i, num // i)
        return sum == num


    # time : O(n ** 0.5)
    # Space complexity : O(1)O(1).


"""
for p = 2:   21(22 − 1) = 6
for p = 3:   22(23 − 1) = 28
for p = 5:   24(25 − 1) = 496
for p = 7:   26(27 − 1) = 8128.

there is only 4 perfect 
"""