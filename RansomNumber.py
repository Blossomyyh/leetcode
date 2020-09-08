from collections import defaultdict


class Solution:

    # MARK : Assume that both strings contain only lowercase letters.


    """brute force simulation """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote: return True
        if not magazine: return False
        if len(ransomNote) > len(magazine): return False
        for i in ransomNote:
            if i not in magazine:
                return False
            loc = magazine.index(i)
            magazine = magazine[:loc] + magazine[loc+1:]
        return True
    """O(N*M) for m ch in ransom, search n times"""



    """HashMap: preprocess magazine"""
    # the problem with the set is it can only contain one instance of any unique charater
    # hashmap --> store ch and its frequencies here
    # should clarify can there be duplicated characters

    def canConstruct2(self, ransomNote, magazine) -> bool:
        """defaultdict --> init all the value type to int"""
        letters = defaultdict(int)
        for c in magazine:
            # increment
            letters[c] += 1
        for n in ransomNote:
            if letters[n] <= 0:
                return False
            # decrement
            letters[n] -= 1

        return True



print(Solution().canConstruct2("aab", "ssddaab"))
print(Solution().canConstruct2(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# True

print(Solution().canConstruct2(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# False