"""
698. Partition to K Equal Sum Subsets
416. Partition Equal Subset Sum


 Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
"""
"""
\\ sol 1: recursively backtracking  --- combination
rec:
    if nums none: return True
    pop ele
    for different groups:
        try add ele
        if < target:
            rec with new groups
            return true if true
            backtrack step --- group - ele 
        if group not 0 and 
"""
nums,k = [4,3,2,3,5,2,1], 4
class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        nums.sort()
        print(nums)
        target, rem = divmod(sum(nums), k)
        # target is the subsum, rem should ==0
        if rem:
            return False
        # print(target, rem,k)

        groups = [0] * k

        def search(groups):
            # print(groups)
            if not nums: return True

            ele = nums.pop()
            for i, group in enumerate(groups):
                if group + ele <= target:
                    groups[i] += ele
                    if search(groups):
                        return True
                    groups[i] -= ele
                # if group is not 0 and didnot return true--> this solution cannot work
                # break -- return false
                if not group:
                    print("if not group")
                    break
            nums.append(ele)
            return False

        return search(groups)



"""
416 partition 2 subset with equal sum

sumup --> get target & rem(0)

"""