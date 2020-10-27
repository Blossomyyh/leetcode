"""
15. 3Sum -- 3 of them add to 0
167. Two Sum II - Input array is sorted

18. 4Sum
"""


def twoSum(self, numbers, target: int):
    l, h = 0, len(numbers) - 1

    while l < h:
        s = numbers[l] + numbers[h]
        if s < target:
            l += 1
        elif s == target:
            return [l + 1, h + 1]
        elif s > target:
            h -= 1
    return []
#################################
"""
\\ sort + 2 pointer

1 should be the least 2,3 should bigger than 1

check whether 1==0 and num1<0
    then do 2 sum
        == 0:
            append and +2, -3
            while 2 not duplicate with previous one [l-1]
                +2
            while 2 not duplicate with next one [h+1]
                -3
        <0:
            +2
        >0:
            -3
time : nlogn + n * n(2 p) -> O(n2)
space : O(1)



"""
def sum3(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if nums[i]>0:
            break
        elif i ==0 or nums[i-1]!= nums[i]:
            # 2 sum with 2 p
            print("in")
            l = i+1
            h = len(nums)-1
            while l<h<len(nums):
                s = nums[i]+nums[l] + nums[h]
                print(i,l,h, s)
                if s==0:
                    result.append([nums[i],nums[l],nums[h]])
                    l += 1
                    h -= 1
                    while l<h and nums[l] == nums[l-1]:
                        l += 1
                    while l<h and nums[h] == nums[h+1]:
                        h -= 1
                elif s<0:
                    l += 1
                elif s>0:
                    h -= 1

    return result

print(sum3([-1,0,1,2,-1,-4]))

"""
\\ hashmap solution
    use set to record duplicationn
    
time O(n2)
space O(n)
"""
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums, i: int, res):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1


################################
"""
4 sum

no need to add too many constrains

"""


def sum4(nums, target):
    result = []
    nums.sort()
    def findNsum(nums, target, N, res):
        if len(nums)<N or N<2 or target<nums[0]*N or target>nums[-1]*N:
            return
        elif N ==2:
            l, r = 0, len(nums)-1
            while l<r:
                s = nums[l] + nums[r]
                if s == target:
                    result.append(res + [nums[l], nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                elif s<target:
                    l+= 1
                else:
                    r -= 1
        else:
            # N==3
            for i in range(len(nums)-N+1):
                if i ==0 or (i>0 and nums[i-1]!= nums[i]):
                    findNsum(nums[i+1:], target - nums[i], N-1, res+[nums[i]])
    findNsum(nums, target, 4, [])
    return result


def fourSum(self, nums, target: int):
    nums.sort()
    result = []
    print(nums)

    def sumfor3(m):
        for i in range(m + 1, len(nums)):
            # print(m, i)
            if i == m + 1 or nums[i - 1] != nums[i]:
                # 2 sum with 2 p
                # print("in")
                l = i + 1
                h = len(nums) - 1
                while l < h < len(nums):
                    s = nums[m] + nums[i] + nums[l] + nums[h]
                    # print(m, i, l, h, s)
                    if s == target:
                        result.append([nums[m], nums[i], nums[l], nums[h]])
                        l += 1
                        h -= 1
                        while l < h and nums[l] == nums[l - 1]:
                            l += 1
                        while l < h and nums[h] == nums[h + 1]:
                            h -= 1
                    elif s < target:
                        l += 1
                    elif s > target:
                        h -= 1

    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            sumfor3(i)
    return result
print(fourSum([1, 0, -1, 0, -2, 2], 0))
