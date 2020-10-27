import re

class Solution(object):

    """
    String Algorithm

    1. Regex
    2.

    You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

    Input: "abab"
    Output: True
    Explanation: It's the substring "ab" twice.

    Input: "aba"
    Output: False

    Input: "abcabcabcabc"
    Output: True
    Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

    """

    """
    1. Regex
    
            Time complexity: {O}(N^2) 
        because we use greedy regex pattern. Once we have a +, the pattern is greedy.
        
        The worst-case situation here is to check all possible pattern lengths from N to 1 that would 
        result in \mathcal{O}(N^2)O(N 2 ) time complexity.
        
        Space complexity:{O}(1)O(1).
    """

    def repeatedSubstringPatternRE(self, s: str) -> bool:
        pattern  = re.compile()
        """
        r - use raw strings to avoid problems with special ch
        ^ from start
        $ to end
        (.+) group of ch --> one or more chs
        \1+ match 1 or more repetitions of the preceding group ( ) 
        this one mark the group --> name as 1 and + has multiple same group    
        """
        t = re.search(r"^(.+)\1+$", s)
        print(t)
        if not t:
            return False
        return True


    """
    2. Find Divisors + Rabin-Karp
        \\Rabin-Karp is a linear-time \mathcal{O}(N)O(N) string searching algorithm:
        
        https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
            
            \\Move a sliding window of length LL along the string of length NN.
            \\Check hash of the string in the sliding window.
            
        For the current problem the standard hash / hashCode 
        is enough because the idea is to check only lengths L,
        which are divisors of N. This way we're not sliding, we're jumping:
        
        To copy characters in sliding window takes time L, 
        to compute hash - time L as well. In total,
         there are N / L substrings, that makes it all work in a linear time \mathcal{O}(N)O(N).

    
    Fractionns 1／3→a（one）third
2／3→two thirds w
    """
    def repeatedSubstringPatternRabin(self, s):
        n = len(s)
        if len(s)< 2 : return False
        if len(s)==2 : return s[0]==s[1]
        #  divisor function can be less than root n
        # cubic root of n^(1/3)
        # (square) root of n n^(1/2)
        for i in range(int(n**0.5), 0, -1):
            #
            if n % i == 0:
                # don't include n
                divisors = [i]
                if i != 1:
                    divisors.append(n//i)
                for divisor in divisors:
                    curHash = initHash = hash(s[:divisor])
                    time = 1
                    while time<n//divisor and curHash == initHash:
                        curHash = hash(s[divisor: divisor*time])
                        time += 1
                    if time == n//divisor and curHash == initHash:
                        return True
        return False




    """
    3. Concatenation
        Repeated pattern string looks like PatternPattern, and the others like Pattern1Pattern2.
        Let's double the input string
        Now let's cut the first and the last characters in the doubled string:
        It's quite evident that if the new string contains the input string, 
        the input string is a repeated pattern string.
        
        Time complexity: \mathcal{O}(N^2)O(N 2) because of the way in and contains are implemented.
        Space complexity: \mathcal{O}(N)O(N), the space is implicitly used to keep s + s string.
        
        cubic root of n^(1/3)
        (square) root of n n^(1/2)
    """
    def repeatedSubstringPatternCon(self, s):
        return s in (s+s)[1:-1]



    """
    4. Knuth-Morris-Pratt Algorithm (KMP)
    
    
    """


print(Solution().repeatedSubstringPatternRabin("abcab"))


