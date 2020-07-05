class Solution:
    # consider whitespace & not capitalization
    def isPalindrome(self, s: str) -> bool:
        # two pointer
        """if there is no character: is Palindrome！！！！"""
        if not s or len(s) == 0: return True
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
                continue
        return True



        # Time complexity:

        # Both s and e are moved inward at every iteration of the while loop and the loop terminates when
        # they meet or cross, so there will be at most n/2 = O(n) iterations. Each iteration of the loop takes
        # constant time, so the loop takes a total of O(n) * O(1) = O(n) time. The rest of the algorithm also takes
        # constant time, so the total time complexity is O(n)

        # Space complexity: The only extra space used is for the two pointers, s and e, so our space complexity is O(1).

    """
    Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
    """

    def validPalindrome(self, s: str) -> bool:

        #         two pointer
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif s[i] != s[j]:
                #  since we can dele one of i/j,
                #  could use parse to create 2 new string and compare the rest of the string
                tmp1 = s[:i] + s[i + 1:]
                tmp2 = s[:j] + s[j + 1:]
                # use [::-1] reverse func to find out whether those are palindrome
                return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]
        return True

    """greedy solution"""
    """all() in python"""
    #     returns True if all items in an iterable are true, otherwise it returns False.
    #   0 / False --> False
    #   dictionary --> check all keys are true (no 0), not values



    def Palindrome(self, s: str) -> bool:
        #         greedy

        """inner function!!"""

        def isPalinRange(i, j):
            return all(s[k] == s[j - k + i] for k in range(i, j))

        """len(s)/2   if 5/2--> 2; 4/2-->2"""
        half = int(len(s) / 2)
        for i in range(half):
            """i in (0,2) --> s[0]===s[-0] should use len(s)-1-i"""
            if s[i] != s[len(s)-1-i]:
                j = len(s) - 1 - i
                return isPalinRange(i + 1, j) or isPalinRange(i, j - 1)
        return True




Solution().Palindrome("abc")
