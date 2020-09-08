"""
1395. Count Number of Teams
You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

"""
"""red black tree"""
import bisect
from typing import List


class Solution:
    # Version A:  [Top Speed] O(n log n) solution using
    # SortedLists to calculate our 4 counting variables in Log(n) time.

    def findLowHigh(self, l, x):
        """
        count number of values higher or and lower than x
        :param rating:
        :param x:
        :return:
        """
        low = bisect.bisect_left(l, x)
        # need to use [len-index]!!! to get the numbers!!
        high = len(l) - bisect.bisect_right(l, x)
        return low, high

    """binary search for bisect ---> O(logn)"""

    def numTeams(self, rating: List[int]) -> int:
        left = []
        right = sorted(rating)
        # we make left and right sorted, so after using bisect-> we can get the num of
        # how many element low/high than x as return index
        res = 0
        for x in rating:
            right.remove(x)
            lowLeft, highLeft = self.findLowHigh(left, x)
            lowRight, highRight = self.findLowHigh(right, x)
            res += lowLeft * highRight + highLeft * lowRight

            left.append(x)
            left.sort()
        #     should make left and right all sorted---> traversal the list,
        #  the element we want to transfer is not sorted
        return res

    """
    The code below simply loops through the array taking an element "x" as the pivot. Using this pivot, we count separately:

    The number of values lower than "x" to the left (loL)
    The number of values higher than "x" to the left (hiL)
    The number of values lower than "x" to the right (loR)
    The number of values higher than "x" to the right (hiR)
    These values are then combined to update our result variable:
    
    result += loL * hiR + hiL * loR
    Everything makes a lot of sense after a moment.
    
    Now, the 4 tracked variables can be obtained in two ways:
    
    The best way is to use SortedLists containing all the values to the Left and Right of our pivot. 
    Using binary search, we can find the index of our pivot in these lists, 
    and quickly deduce the number of elements higher or lower. 
    This allows us to have a O( n log n ) solution.
    
    Otherwise, we can use two nested loops to build our counting variables primitively. 
    
    This gives us a O(n^2) solution.
    Both code versions are presented below. I hope the explanation was helpful. Cheers,

    """


print(Solution().numTeams([2, 5, 3, 4, 1]))


# Version B:  O(n^2) solution with (primitive) nested loops for building our 4 counting variables.
class Solution:
    def numTeamsbrute(self, A)-> int:
        length = len(A)
        res = 0
        if length < 3: return 0
        for j in range(1, length -1):
            x, lowLeft, lowRgiht, highLeft, highRight = A[j], 0, 0, 0, 0
            for i in range(j):
                if A[i] < x:
                    lowLeft += 1
                if A[i] > x:
                    highLeft += 1
            for i in range(j+1, length):
                if A[i] < x:
                    lowRgiht += 1
                if A[i] > x:
                    highRight += 1
            res += lowRgiht * highLeft + highLeft * lowRgiht
        return res
