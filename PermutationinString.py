"""
567. Permutation in String

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

first get all ord(character) for 2 string
construct target [0]*26
using sliding window (size fixed):
    add new ele in window
    if idx > length:
        delete the first one -- [idx- windowsize]
    if target == window
        True
    False

"""
def checkInclusion(self, s1: str, s2: str) -> bool:
    A = [ord(s)-ord('a') for s in s1]
    B = [ord(s)-ord('a') for s in s2]

    # transfer 2 string to integer
    # construct list to compare
    target = [0]*26
    for i in A:
        target[i] += 1
    print(target)

    window = [0]*26
    for i, x in enumerate(B):
        window[x] += 1
        if i>=len(A):
            window[B[i-len(A)]] -= 1
        if window == target:
            return True
    return False

