def isBadVersion(param):
    return False


class Solution:

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        if isBadVersion(1):
            return 1
        while low <= high:
            mid = low + (high-low)//2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif not isBadVersion(mid):
                low = mid+1
            else:
                high = mid-1
        return -1

    """
    We can check with a linear scan.
    sum in compare
    
    """
    def numsJewelsLinerStones(self, J: str, S: str):
        return sum(s in J for s in S)

    """
    set in Python
    Time Complexity:O(J.length+S.length))
    """
    def numsJewelsInStones(self, J: str, S: str):
        Jset = set(J)
        return sum(s in Jset for s in S)

if __name__ == "__main__":
    print("hello word")