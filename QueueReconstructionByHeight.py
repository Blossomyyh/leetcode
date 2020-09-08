"""
406. Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue.
Each person is described by a pair of integers (h, k),
where h is the height of the person
and k is the number of people in front of this person who have a height greater than or equal to h.
Write an algorithm to reconstruct the queue.

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


The number of people is less than 1,100.

sort the array by some sequence



**** understand lower height people is invisible to higher height people***
only need to focus on first sort the people by the height
process the people who are tallest
put person with less k at second sort
-> essentially, order by the k as well
go through person by person and constructing the array
if a[0]>b[0] or a[1]<b[1]


time complexity:
bound by sort time quick/merge nlogn
insertion o(n) time

"""
from typing import List
class Solution():
    def QueueReconstructionHeight(self, input: List[List]):
        input.sort(key=lambda x : (-x[0], x[1]))

        res = []
        for person in input:
            res.insert(person[1],person)
        return res

input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(Solution().QueueReconstructionHeight(input))
# [[5,0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]