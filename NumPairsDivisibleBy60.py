"""
To go on with the solution of this problem,
we first need to understand the terms remainder and complement as used in this context.

For a value n, the remainder is what remains after n/60. (ie. n % 60).
For a value n, the complement is the required number whose sum with n is divisible by 60:
Note that the remainder of a value can be the complement of another value. For such two values,
they form a pair.
Example for a number 85,
its remainder is 25 and its complements are x = (35, 95, 155,...,x+60).
In other words, for an integer k, if the value of k % 60(remainder of k) is 35,
then the number is a complement of 85. Therefore, 85 forms a pair with all values in set x.
These complements , k%60, ranges from 0 to 59.

Now lets map all these complements to their count.
 We can use an array since the complements are integers from 0 t0 59. First initialize their counts to 0;

Logic
For each value n in the array, calculate its remainder and its complement.
If its complement is in the map, then you have two pairs whose sum is divisible by 60.

Now lets talk about how we know the complement of the value n is in the map.
We do this by incrementing the count of each value's remainder after every iteration. So that on the ith value, the count of its complement in the map will determine the number of previous values that form a pair with it

"""

from typing import List


# 1010. Pairs of Songs With Total Durations Divisible by 60
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = {}
        result = 0
        for t in time:
            remainder = t % 60
            # find complement 60-remainder is in dictionary
            """notice : we should (60-remainder)% 60 !!! as well since the remainder only 0-59 not 60!!"""
            if (60 - remainder) % 60 in count:
                result += count[(60 - remainder) % 60]
            count[remainder] = count.get(remainder, 0) + 1

        return result

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = {}
        for t in time:
            remainder = t % 60
            count[remainder] = count.get(remainder, 0) + 1
        res = 0
        for value in count:
            # edge -- 0 and 30 has complement as itself, so do Cn ^2
            if value == 0 or value == 30:
                res += count[value] * (count[value] - 1) // 2
            # other half of them just multiple itself with
            elif value < 30 and 60 - value in count:
                res += count[value] * count[60 - value]
        return res


print(Solution().numPairsDivisibleBy60([60, 60, 60]))
