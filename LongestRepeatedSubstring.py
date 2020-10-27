"""
1062. Longest Repeating Substring

"""
"""
\\ binary search + hashmap

binary search --> search for length from middle until start>end
    if can get repeated substring:
        increase start
    else
        decrease end
after get length use hashset --> record each substring and compare seen or not

\\ Time complexity :O(NlogN) in the average case 
                    O(N 2) in the worst case - n the worst case of L close to N/2
    Space complexity : O(N) to keep the hashset.
"""
def search(L: int, n: int, S: str):
    """
    Search a substring of given length
    that occurs at least 2 times.
    @return start position if the substring exits and -1 otherwise.
    """
    seen = set()
    for start in range(0, n - L + 1):
        tmp = S[start:start + L]
        if tmp in seen:
            return start
        seen.add(tmp)
    return -1


def longestRepeatingSubstring(S: str) -> str:
    n = len(S)

    # binary search, L = repeating string length
    left, right = 1, n
    while left <= right:
        L = left + (right - left) // 2
        if search(L, n, S) != -1:
            left = L + 1
        else:
            right = L - 1

    return left - 1


print(longestRepeatingSubstring("abbaba"))


# rabin karp
class Solution:
    def search(self, L: int, a: int, modulus: int, n: int, nums: List[int]) -> str:
        """
        Rabin-Karp with polynomial rolling hash.
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        # compute the hash of string S[:L]
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % modulus

        # already seen hashes of strings of length L
        seen = {h}
        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)
        return -1

    def longestRepeatingSubstring(self, S: str) -> str:
        n = len(S)
        # convert string to array of integers
        # to implement constant time slice
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2 ** 24

        # binary search, L = repeating string length
        left, right = 1, n
        while left <= right:
            L = left + (right - left) // 2
            if self.search(L, a, modulus, n, nums) != -1:
                left = L + 1
            else:
                right = L - 1

        return left - 1