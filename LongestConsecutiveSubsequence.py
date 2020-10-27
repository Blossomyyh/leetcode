"""
128. Longest Consecutive Sequence
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

"""
\\ sorting with memorization
sort the list
single path:
    ignore when cur == pre (length will has no change on it!!)
    compare cur == pre +1
        yes -- incre num
        no -- save max length
return max

time : nlogn
space : 1
"""
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        maxlen = 0
        curlen = 1
        print(nums)
        for i in range(len(nums)):
            if nums[i-1] != nums[i]:
                if nums[i-1]+1 == nums[i]:
                    curlen += 1
                else:
                    maxlen = max(maxlen, curlen)
                    curlen  = 1
            print(curlen, maxlen)
        maxlen = max(maxlen, curlen)
        return maxlen


"""
\\ set() for search + find the smallest to begin

create set for searching
find smallest in sequence : num-1 not in set:
    while num in set:
        increment num
        increment length
    save max
    
    
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)

        for num in numset:
            if num - 1 not in numset:
                curnum = num
                current = 1
                while curnum + 1 in numset:
                    current += 1
                    curnum += 1
                longest = max(current, longest)

        return longest

"""
Time complexity : O(n)O(n).
reveals it to be linear. 
Because the while loop is reached only when currentNum marks the beginning of a sequence
 (i.e. currentNum-1 is not present in nums),
  the while loop can only run for n iterations 
  throughout the entire runtime of the algorithm.
  
Space complexity : O(n)O(n).


"""