"""
135. Candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""
"""
left : should have candys for the left side
right : should have candys for the right side

get max of left and right
\\ time O(n)
\\ space O(n)

optimization: use one array
"""

# 14
# [12,3,3,11,34,34,1,67]
class Solution:
    def candy(self, ratings) -> int:
        if not ratings: return 0
        if len(ratings) == 1: return 1
        left = [1] * len(ratings)
        right = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                left[i] = left[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                right[i] = right[i + 1] + 1
        res = 0

        for i in range(len(ratings)):
            res += max(left[i], right[i])

        return res