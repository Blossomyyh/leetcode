from typing import List

"""
solution 1:
sort + compare adjacent
"""

"""
    solution 2:
    dic / map
"""


def findDuplicates(nums: List[int]) -> List[int]:
    if len(nums) < 1:
        return
    dic = {}

    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    # clear for delete all element of List
    nums.clear()
    for vals in dic:
        if dic[vals] > 1:
            nums.append(vals)

    return nums


'''
    1. initialize a dictionary 
    2. traverse the list looking at every element, and if that element is already in the map, increment its count
    3. once done, return an array of all the elements that had duplicates


        time: O(N)  [2 O(N) === O(N)]
        space: O(N) => only made a dictionary ! cleared and re-used the nums list

        i am still learning the whole time complexity analysis, so, please for more experienced programmers, correct my time/space analysis if need be. In the meantime, I am going to go watch Nick Whites solution

'''

"""
set
"""


def findDuplicates(self, nums: List[int]) -> List[int]:
    if len(nums) < 1:
        return

    res = set()
    single = set()

    for i in nums:
        if i in single:
            res.add(i)
        else:
            single.add(i)

    return list(res)


def findSDuplicates(nums: List[int]) -> List[int]:
    res = set()
    for i in range(len(nums)):
        while nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        if nums[i] - 1 != i and nums[nums[i] - 1] == nums[i]:
            res.add(nums[i])
    return list(res)


findDuplicates([1, 2, 3, 3, 4, 4, 5, 5, 3])

"""
Mark Visited Elements in the Input Array itself
"""


def findDuplicates(self, nums: List[int]) -> List[int]:
    if len(nums) < 1:
        return

    res = set()

    for i in nums:
        nums[abs(i) - 1] *= -1
    for i in nums:
        if nums[abs(i) - 1] > 0:
            res.add(abs(i))
            nums[abs(i) - 1] *= -1

    return list(res)
