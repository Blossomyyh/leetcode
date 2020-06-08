from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums) - 2, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        # If we get as far as the last element,
        # we know that it must be the single element.
        return nums[-1]

        # Time complexity : O(n)

        # Space complexity : O(1)O(1).

    """
    binary search
    single should be in odd part
    
    """

    # 1.find mid
    # 2.determine the odd/ evenness of the sides and set lo and hi to cover the part of the array
    # 3. draw diagram -- avoid off-by-one errors 只差一位的错误
    def singleNonDuplicate(self, nums: List[int]) -> int:
        even = len(nums)
        high = len(nums) - 1
        low = 0
        while high > low:
            mid = low + (high - low) // 2
            left_are_even = (high - mid) % 2 == 0
            if nums[mid] == nums[mid + 1]:
                if left_are_even:
                    low = mid + 2
                else:
                    high = mid - 1
            elif nums[mid] == nums[mid - 1]:
                if left_are_even:
                    high = mid - 2
                else:
                    low = mid + 1
            else:
                return nums[mid]
        return nums[low]


        # Time complexity : O(logn)
        # Space complexity : O(1)O(1).


    """
    mid index is even/ odd matters
    """
# 1.find mid
# 2.determine by mid is even/ odd and its number
    def singleNonDuplicate(self, nums: List[int]) -> int:
        even = len(nums)
        high = len(nums)-1
        low = 0
        while(high>low):
            mid = low + (high-low)//2
            if mid % 2 ==1:
                mid -=1
            if nums[mid]==nums[mid+1]:
                low = mid +2
            else:
                high = mid
        return nums[low]