# Easy Solution Using Prefix Sum
from typing import List
from collections import defaultdict


class Solution(object):
    def subarraysDivByK1(self, A, K):
        res = 0
        count = 0
        letter = defaultdict(int)
        letter[0] = 1
        for i in A:
            res+=i
            if res%K in letter:
                count+= letter[res%K]
            letter[res%K] += 1
        return count

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        sumR = res = 0
        dic = defaultdict(int)
        dic[0] = 1

        for i in A:
            sumR += i
            dic[sumR % K] = dic.get(sumR % K, 0) + 1
        # for v in dic.values():
        #     res += (v * (v - 1) // 2)
        return sum(v * (v - 1) // 2 for v in dic.values())

        # P = [0]
        # for x in A:
        #     P.append((P[-1] + x) % K)
        #
        # count = collections.Counter(P)
        # print(count.keys())
        # print(count.values())
        # return sum(v * (v - 1) // 2 for v in count.values())

Solution().subarraysDivByK([4,5,0,-2,-3,1], 5)
"""
Given an array of integers and an integer k, 
you need to find the total number of continuous subarrays whose sum equals to k.
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hsh = {0: 1}
        count = sum = 0

        for num in nums:
            sum += num

            if sum - k in hsh:
                count += hsh[sum - k]

            hsh[sum] = hsh.get(sum, 0) + 1

        return count