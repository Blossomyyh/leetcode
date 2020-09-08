from typing import List
class Solution:
    """iteration"""
    # twice binary search
    # write binary search with a little twist!!
    def binarySearch(self, nums: List[int], target, low, high, findFirst):
        while low <= high:
            mid = low + (high-low)//2
            if findFirst:
                if (mid == 0 or target > nums[mid-1]) and target == nums[mid]:
                    return mid
                elif target > nums[mid] :
                    low = mid +1
                else:
                    # 2 condition: 1. target <mid 2. == but not the leftmost
                    high = mid - 1
            else:
                if (mid == len(nums)-1 or nums[mid+1]> target) and nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1

        return -1



    """recursive"""
    def binarySearchRe(self, nums: List[int], target, low, high, findFirst):
        # cannot find any
        if high < low:
            return -1
        mid = low + (high - low) // 2
        if findFirst:
            if (mid == 0 or target > nums[mid - 1]) and target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return self.binarySearchRe(nums, target, mid + 1, high, findFirst)
            else:
                # 2 condition: 1. target <mid 2. == but not the leftmost
                return self.binarySearchRe(nums, target, low, mid -1, findFirst)
        else:
            if (mid == len(nums) - 1 or nums[mid + 1] > target) and nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return self.binarySearchRe(nums, target, low, mid -1, findFirst)
            else:
                return self.binarySearchRe(nums, target, mid + 1, high, findFirst)


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.binarySearch(nums, target, 0, len(nums)-1, True)
        last = self.binarySearch(nums, target, 0, len(nums)-1, False)
        return [first, last]
