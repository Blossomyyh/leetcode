"""
78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
Input: nums = [1,2,3]
Output:
[[3],[1],[2], [1,2,3], [1,3], [2,3], [1,2],[]]
"""
'''
\\ 1. Backtracking
dfs
idx, cur
each dfs -> append cur into result
then -> for n in range idx, end: 
            (assume all num is unique)
            Gonna Proceed to add more integers into the combination 
             then do dfs(n, cur+ [n]) 
#########
 1,2,3 all distinct
[]
1 1,2 1,2,3
  1,3
2 2,3
3
########
\\ time complexity: N* 2^N ---- since each element could be absent or present for n length
    space the same: subsets multiplied by the number N length to keep for each subset.
'''

# 0+n+n*(n-1)+++ n**n --> O(n^n)
# n^3
nums = [1,2,3]

# assume nums are all distinct!
def subsets(nums):
    if not nums: return []
    if len(nums)==1: return [[], nums]

    result = []
    def dfs(l, cur,first, curset):
        if len(cur) == l:
            result.append(cur)
            return

        for i in range(first, len(nums)):
            if nums[i] not in curset:
                curset.add(nums[i])
                print(l, cur + [nums[i]], i+ 1)
                dfs(l, cur + [nums[i]], i+ 1 , curset)
                curset.remove(nums[i])
    for x in range(len(nums)+1):
        curset = set()
        dfs(x, [],0, curset)
    return result
# print(subsets(nums))


def subsetUnique(nums):
    result = []

    def dfs(idx, path):
        result.append(path)
        for i in range(idx, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result

'''
\\ 2. Cascading
At each step we take a new integer into consideration
0[]
1[1]
2[2], [1,2]
3[3], [1,3], [2,3], [1,2,3]

time/space complexity: N* 2^N
'''
def subsetCas(sums):
    result = [[]]
    for i in nums:
        newlist = []
        for l in result:
            newlist.append(l + [i])
        result.extend(newlist)

    output = [[]]
    for i in nums:
        output += [cur+[i] for cur in output]
    return result, output
print(subsetCas(nums))


'''
\\ 3. Bit manipulation

Lexicographic (Binary Sorted) Subsets --- Bitmask : 010 == x2x

- generate all possible binary bitmasks of length n. for 0/1
- map a subset to each bitmask --  ith position in bitmask means the presence of num[i] 0-x, 1-y
- return output
time/space complexity: N* 2^N

'''


def subsetsBit( nums):
    n = len(nums)
    output = []
    nth_bit = 1 << n
    print(nth_bit) #8
    for i in range(2 ** n):
        # generate bitmask, from 0..00 to 1..11
        bitmask = bin(i | nth_bit)[3:]
        print(bitmask)
        '''
        000 001 010 011 100 101 110 111
        '''

        # append subset corresponding to that bitmask
        output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

    return output



"""
\\ 90. Subsets II

Given a collection of integers that might contain duplicates, nums,
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
Input: [1,2,2]
Output:
[[2],[1], [1,2,2],[2,2], [1,2], []]

\\ time: N* 2^N
"""
"""
dfs recursively construct substring
################
subset --> no sequence restriction
###############
not distinct --> duplication --> sort
#####################################################################

start from idx = 0, 
\\ dfs function
\\ 1.append cur path to list
\\ 2.for each iteration(idx, list)
        go single path for ele behind it
            add ele at a time
            (move idx forward + 1)
            iterate with idx+1 and list+[curele]

        \\#duplication will come after the first iteration
        #############
        check ele>idx and nums[ele]!=nums[ele-1](same elements should be together)
        ########
    return 
"""

from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ## RC ##
        ## APPROACH : BACKTRACKING ##
        ## Similar to Leetcode : 47. Permutations II ##

        ## TIME COMPLEXICITY : O(2^N) ##
        ## SPACE COMPLEXICITY : O(2^N) ##

        nums.sort()
        # sort to make duplication be together 12223
        result = []

        def dfs(idx, path):
            result.append(path)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])

        return result