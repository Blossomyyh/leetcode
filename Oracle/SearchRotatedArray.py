def search(self, nums: List[int], target: int) -> int:

    s, e = 0, len(nums) - 1
    while s <= e < len(nums):
        m = (s + e) // 2
        if nums[m] == target:
            return m
        elif nums[m] >= nums[s]:
            if target >= nums[s] and target < nums[m]:
                e = m - 1
            else:
                s = m + 1
        else:
            if target <= nums[e] and target > nums[m]:
                s = m + 1
            else:
                e = m - 1
    return -1



"""
Now there could be two situations:
\\start<mid<small<end
     - If the target is located in the non-rotated subarray: 
  go left: `end = mid - 1`.
  
  - Otherwise: go right: `start = mid + 1`.
  
\\start<small<mid<end
      - If the target is located in the non-rotated subarray: 
  go right: `start = mid + 1`.
  
  - Otherwise: go left: `end = mid - 1`.
  


"""